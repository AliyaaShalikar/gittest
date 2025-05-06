import socket

HOST = '192.168.80.216' 
PORT = 8888       

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address
server_socket.bind((HOST, PORT))

# Enable the server to accept connections (max 5 clients in the queue)
server_socket.listen(5)

print(f"Server started on {HOST}:{PORT}. Waiting for a connection...")

# Accept a connection from a client
client_socket, client_address = server_socket.accept()
print(f"Connection established with {client_address}")

# Chat loop for communication between server and client
while True:
    # Receive the message from the client
    message = client_socket.recv(1024).decode()
    if message.lower() == 'exit':
        print("Client requested to exit. Closing the connection.")
        break

    print(f"Client: {message}")
    
    # Server responds back
    response = input("Server: ")
    client_socket.send(response.encode())
    
    if response.lower() == 'exit':
        print("Server exiting the chat.")
        break

# Close the sockets
client_socket.close()
server_socket.close()