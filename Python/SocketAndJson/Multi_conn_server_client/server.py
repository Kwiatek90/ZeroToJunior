import sys
import socket
import selectors
import types

# Funkcja obsługująca przyjmowanie połączeń
def accept_wrapper(sock):
    # Akceptuj przychodzące połączenie (blokujące operacje)
    conn, addr = sock.accept()
    print(f"Przyjęto połączenie od {addr}")
    conn.setblocking(False)  # Ustaw gniazdo na tryb nieblokujący
    # Utwórz obiekt SimpleNamespace do przechowywania danych związanych z połączeniem
    data = types.SimpleNamespace(addr=addr, inb=b"", outb=b"")
    # Zarejestruj gniazdo z selektorem, aby monitorować zarówno zdarzenia odczytu, jak i zapisu
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    sel.register(conn, events, data=data)

# Funkcja obsługująca połączenia
def service_connection(key, mask):
    sock = key.fileobj
    data = key.data
    if mask & selectors.EVENT_READ:  # Jeśli gniazdo gotowe do odczytu
        recv_data = sock.recv(1024)  # Odbierz dane od klienta (blokujące operacje)
        if recv_data:
            data.outb += recv_data  # Dodaj otrzymane dane do bufora wyjściowego
        else:
            print(f"Zamknięcie połączenia z {data.addr}")
            sel.unregister(sock)  # Wyrejestruj gniazdo z selektora
            sock.close()  # Zamknij gniazdo
    if mask & selectors.EVENT_WRITE:  # Jeśli gniazdo gotowe do zapisu
        if data.outb:
            print(f"Wysyłanie {data.outb!r} do {data.addr}")
            sent = sock.send(data.outb)  # Wyślij dane do klienta (blokujące operacje)
            data.outb = data.outb[sent:]  # Usuń wysłane dane z bufora wyjściowego

# Inicjalizacja selektora
sel = selectors.DefaultSelector()

# Pobranie hosta i portu z argumentów wiersza poleceń
host, port = sys.argv[1], int(sys.argv[2])

# Tworzenie gniazda nasłuchującego
lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
lsock.bind((host, port))
lsock.listen()
print(f"Nasłuchiwanie na {(host, port)}")
lsock.setblocking(False)  # Ustaw gniazdo na tryb nieblokujący

# Rejestracja gniazda nasłuchującego w selektorze
sel.register(lsock, selectors.EVENT_READ, data=None)

try:
    while True:
        events = sel.select(timeout=None)
        for key, mask in events:
            if key.data is None:
                accept_wrapper(key.fileobj)  # Obsługa nowego połączenia
            else:
                service_connection(key, mask)  # Obsługa istniejącego połączenia
except KeyboardInterrupt:
    print("Przechwycono przerwanie klawiatury, zamykanie")
finally:
    sel.close()  # Zamknięcie selektora
