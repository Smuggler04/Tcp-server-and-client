import socket 

def server_program():
    # define host and port
    host = socket.gethostname()
    port = 5000

    # get instance of socket and bind port and host together 
    server_socket = socket.socket()
    server_socket.bind((host,port))


    # accept new connection 
    server_socket.listen(2)
    conn, address = server_socket.accept()
    print("connection from: " + str(address))
    
    
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print(str(data))

        data = input('->')
        if data == "close":
            break
        
    
        conn.send(data.encode())
    conn.close()

if __name__ == '__main__':
    server_program()