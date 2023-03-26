import socket

def client_program():
    host = "127.0.0.1"
    port = 5000

    # initiate instance and connect to server
    client_socket = socket.socket()
    client_socket.connect((str(host), port))

    # take input
    message = input('->')

    while message.lower().strip() != 'close':
        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()

        print(data)

        message = input('->')

    client_socket.close()


if __name__ == '__main__':
    client_program()

