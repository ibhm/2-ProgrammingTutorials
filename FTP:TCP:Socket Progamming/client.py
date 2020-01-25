from socket import *

serverName = ''
serverPort = 12000

s = socket(AF_INET, SOCK_STREAM)
s.connect((serverName, serverPort))  # socket between client and proxy
print("Connection to Proxy Server sucessful\n")

BUFFER = 1024


def connectto(actualserver):
    try:
        message = "GET / " + actualserver + " HTTP/1.1\r\n" + \
        "Host: " + serverName + ":" + "\r\n\r\n"
        s.send(message.encode())
        #s.recv(2048).decode()
        print(s.recv(4096).decode())
    except error:
        print("Connecting error")

def user(username):
    try:
        message = "GET / USER " + username +" HTTP/1.1\r\n" + \
        "Host: " + serverName + ":" + "\r\n\r\n"
        s.send(message.encode())

        print(s.recv(4096).decode())
    except error:
        print("Proxy error")


def psswd(password):
    try:
        message = "GET / PASS " + password +" HTTP/1.1\r\n" + \
        "Host: " + serverName + ":" + "\r\n\r\n"
        s.send(message.encode())

        print(s.recv(4096).decode())
    except error:
        print("Proxy error")

def cwd(directory):
    try:
        message = "GET / CWD " + directory +" HTTP/1.1\r\n" + \
        "Host: " + serverName + ":" + "\r\n\r\n"
        s.send(message.encode())

        print(s.recv(4096).decode())
    except error:
        print("Proxy error")

def pwd():
    try:
        message = "GET / PWD HTTP/1.1\r\n" + \
        "Host: " + serverName + ":" + "\r\n\r\n"
        s.send(message.encode())

        print(s.recv(4096).decode())
    except error:
        print("Proxy error")


def help(helpcommand):
    try:
        message = "GET / HELP " + helpcommand +" HTTP/1.1\r\n" + \
        "Host: " + serverName + ":" + "\r\n\r\n"
        s.send(message.encode('utf-8'))

        print(s.recv(4096).decode('utf-8'))
    except error:
        print("Proxy error")


def cdup():
    try:
        message = "GET / CDUP HTTP/1.1\r\n" + \
        "Host: " + serverName + ":" + "\r\n\r\n"
        s.send(message.encode())

        print(s.recv(4096).decode())
    except error:
        print("Proxy error")


def syst():
    try:
        message = "GET / SYST HTTP/1.1\r\n" + \
        "Host: " + serverName + ":" + "\r\n\r\n"
        s.send(message.encode())

        print(s.recv(4096).decode())
    except error:
        print("Proxy error")


def quit():
    try:
        message = "GET / QUIT HTTP/1.1\r\n" + \
        "Host: " + serverName + ":" + "\r\n\r\n"
        s.send(message.encode())

        print(s.recv(4096).decode())
        return -1 
    except error:
        print("Proxy error")


actualserver = input("\nEnter ftp followed by website\n")
connectto(actualserver[4:])

while True:
    cmd = input("\nEnter FTP command\n")
    if cmd[:4].upper() == "USER":
        user(cmd[5:])  # rest of command is username
    elif cmd[:4].upper() == "PASS":
        psswd(cmd[5:])
    elif cmd[:3].upper() == "PWD":
        pwd()
    elif cmd[:3].upper() == "CWD":
        cwd(cmd[4:])
    elif cmd[:4].upper() == "HELP":
        help(cmd[5:])
    elif cmd[:4].upper() == "CDUP":
        cdup()
    elif cmd[:4].upper() == "SYST":
        syst()
    elif cmd[:4].upper() == "QUIT":
        quit()

s.close()
