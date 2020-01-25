from socket import *

BUFFER = 1024
serverPort = 12000

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))  # syntax for becoming server
serverSocket.listen(1)
print("The server is ready to receive")

while True:
    clientconnectionSocket, addr = serverSocket.accept()  # for accepting client socket
    try:
        cmd = clientconnectionSocket.recv(1024).decode()  # recieve message
        ip = gethostbyname(cmd.split()[2])  # ip address of ftp server

        a = socket(AF_INET, SOCK_STREAM)  # for connecting to actual webserver
        a.connect((ip, 21))
        reply = a.recv(1024).decode()
        a.send('USER anonymous\r\n'.encode())  # login details
        reply2 = a.recv(1024).decode()
        a.send('PASS ibhm.792@gmail.com\r\n'.encode())
        reply3 = a.recv(1024).decode()

        if reply3 == '230 User logged in.\r\n':
            message = "HTTP/1.1 200 OK\r\n" + reply3
            clientconnectionSocket.send(message.encode())
        else:
            clientconnectionSocket.send("Connection failed".encode())

        while True:
            ftpcmdorginial = clientconnectionSocket.recv(2048).decode() # ftp command from client 
            ftpcmd = ftpcmdorginial.split()[2]
            if ftpcmd.upper() == "USER":
                username = ftpcmdorginial.split()[3]  # gets username then
                message = "USER "+username+"\r\n"
                a.send(message.encode())
                reply3 = a.recv(1024).decode()
                message = "HTTP/1.1 200 OK\r\nWebsite says " + reply3
                clientconnectionSocket.send(message.encode())

            elif ftpcmd.upper() == "PASS":
                password = ftpcmdorginial.split()[3]  # gets password then
                message = "PASS "+password+"\r\n"
                a.send(message.encode())
                reply3 = a.recv(1024).decode()
                message = "HTTP/1.1 200 OK\r\nWebsite says " + reply3
                clientconnectionSocket.send(message.encode())

            elif ftpcmd.upper() == "PWD":
                a.send("pwd\r\n".encode())
                reply3 = a.recv(1024).decode()
                message = "HTTP/1.1 200 OK\r\nWebsite says " + reply3
                clientconnectionSocket.send(message.encode())
            
            elif ftpcmd.upper() == "CDUP":
                a.send("cdup\r\n".encode())
                reply3 = a.recv(1024).decode()
                message = "HTTP/1.1 200 OK\r\nWebsite says " + reply3
                clientconnectionSocket.send(message.encode())

            elif ftpcmd.upper() == "CWD":
                dir = ftpcmdorginial.split()[3]  # gets directory name then
                message = "cwd "+dir+"\r\n"
                a.send(message.encode())
                reply3 = a.recv(1024).decode()
                message = "HTTP/1.1 200 OK\r\nWebsite says " + reply3
                clientconnectionSocket.send(message.encode())

            elif ftpcmd.upper() == "HELP":
                helpcommand = ftpcmdorginial.split()[3]
                #clientconnectionSocket.send(helpcommand.encode())

                message = "help " + helpcommand + "\r\n"
                a.send(message.encode())
                reply3 = a.recv(4096).decode()
                message = "HTTP/1.1 200 OK\r\nWebsite says " + reply3
                clientconnectionSocket.send(message.encode())

            elif ftpcmd.upper() == "SYST":
                a.send("syst\r\n".encode())
                reply3 = a.recv(1024).decode()
                message = "HTTP/1.1 200 OK\r\nWebsite says " + reply3
                clientconnectionSocket.send(message.encode())

            elif ftpcmd.upper() == "QUIT":
                a.send("quit\r\n".encode())
                reply3 = a.recv(1024).decode()
                message = "HTTP/1.1 200 OK\r\nWebsite says " + reply3
                clientconnectionSocket.send(message.encode())
                a.close()
                clientconnectionSocket.close()

    except IOError:
        clientconnectionSocket.send("HTTP/1.1 404 NOT FOUND \r\n".encode())

    clientconnectionSocket.close()

serverSocket.close()
