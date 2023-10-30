import sys
import socket
import selectors
import types

# Inicjalizacja selektora
sel = selectors.DefaultSelector()

# Lista wiadomości, które klienci będą wysyłać
messages = [b"Message 1 from client,", b"Message 2 from client,"]

# Funkcja rozpoczynająca nawiązywanie połączenia
def start_connection(host, port, num_conns):
    server_addr = (host, port)
    for i in range(0, num_conns):
        connid = i + 1
        print(f"Rozpoczęcie połączenia {connid} z {server_addr}")
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setblocking(False)  # Ustawienie gniazda w tryb nieblokujący
        sock.connect_ex(server_addr)  # Rozpoczęcie próby nawiązania połączenia
        events = selectors.EVENT_READ | selectors.EVENT_WRITE
        data = types.SimpleNamespace(
            connid=connid,  # Numer identyfikacyjny połączenia
            msg_total=sum(len(m) for m in messages),  # Łączna liczba bajtów do odebrania
            recv_total=0,  # Liczba odebranych bajtów
            messages=messages.copy(),  # Kopia listy wiadomości do wysłania
            outb=b""  # Bufor wyjściowy
        )
        sel.register(sock, events, data=data)

# Funkcja obsługująca połączenia
def service_connection(key, mask):
    sock = key.fileobj
    data = key.data
    if mask & selectors.EVENT_READ:  # Jeśli gniazdo gotowe do odczytu
        recv_data = sock.recv(1024)  # Próba odebrania danych (blokujące operacje)
        if recv_data:
            print(f"Odebrano {recv_data!r} z połączenia {data.connid}")
            data.recv_total += len(recv_data)
        if not recv_data or data.recv_total == data.msg_total:
            print(f"Zamknięcie połączenia {data.connid}")
            sock.close()
    if mask & selectors.EVENT_WRITE:  # Jeśli gniazdo gotowe do zapisu
        if not data.outb and data.messages:
            data.outb = data.messages.pop(0)
        if data.outb:
            print(f"Wysyłanie {data.outb!r} do połączenia {data.connid}")
            sent = sock.send(data.outb)  # Próba wysłania danych (blokujące operacje)
            data.outb = data.outb[sent:]

# Sprawdzenie liczby argumentów wiersza poleceń
if len(sys.argv) != 4:
    print(f"Użycie: {sys.argv[0]} <host> <port> <liczba_połączeń>")
    sys.exit(1)

# Parsowanie argumentów wiersza poleceń: host, port i liczba połączeń
host, port, num_conns = sys.argv[1:4]

# Rozpoczęcie nawiązywania połączeń z serwerem
start_connection(host, int(port), int(num_conns))

try:
    while True:
        # Monitorowanie operacji wejścia/wyjścia na gniazdach (z timeoutem 1 sekundy)
        events = sel.select(timeout=1)
        if events:
            for key, mask in events:
                service_connection(key, mask)
        # Sprawdzenie, czy nadal istnieją gniazda monitorowane przez selektor
        if not sel.get_map():
            break
except KeyboardInterrupt:
    print("Przechwycono przerwanie klawiatury, zamykanie")
finally:
    sel.close()  # Zamknięcie selektora
