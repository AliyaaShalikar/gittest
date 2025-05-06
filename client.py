# tcp_client.py

import socket

HOST = '172.16.0.97'  # Server IP (localhost)
PORT = 8888         # Port to connect to

# Create a TCP socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))  # Connect to server
    client_socket.sendall(b'Hello, server!')
    data = client_socket.recv(1024)
    print(f"[CLIENT] Received from server: {data.decode()}")
