# echo-client.py
# cd Python\SocketAndJson\Echo_client_and_server
   
import socket

HOST = "127.0.0.1" # Th server's hostname  or Ip address
PORT = 65432 # The port  used by  the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"Hello world")
    data = s.recv(1024)
    
print(f"Recived {data!r}")