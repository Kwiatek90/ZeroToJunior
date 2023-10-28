# echo-server.py

import socket

HOST = "127.0.0.1" # Standard loopback interface addres (localhost)
PORT = 65432 # Port to listen on  (non-privileged ports are > 1023)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT)) #towrzy serwer
    s.listen() # nasluchuje czy ktos sie laczy
    conn, adr = s.accept() #pobiera adrress i conn z polaczenia
    with conn:
        print(f"Connected: {adr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
            
        