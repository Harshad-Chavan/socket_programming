# Import socket module
import socket

# Create a socket object
s = socket.socket()

# Define the port on which you want to connect
port = 80
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
# connect to the server on local computer
s.connect(('127.0.0.1', port))
s.send(IPAddr.encode())
reply = s.recv(1024).decode()
print(reply)
while True:
    x = input("enter some text:" + "\n")
    s.send(x.encode())
    reply = s.recv(1024).decode()
    print(reply)
    if reply == 'bye':
        break

s.close()
