
import socket
mesg_list = ["hi"]
try:
    socket_obj = socket.socket()
    print("socket created succesfully")

    port = 80

    socket_obj.bind(('', port))
    socket_obj.listen(5)

    while True:
        c, address = socket_obj.accept()
        client_ip = c.recv(1024)
        print("{0} has connected".format(client_ip.decode()))
        c.send(("welcome to the chat bot").encode())
        while True:
            x = c.recv(1024)
            if x.decode() == "bye":
                c.send(("see you soon bye !!").encode())
                print("{0} has dis-connected".format(client_ip.decode()))
                c.close()
                break
            rev_x = x.decode()[::-1]
            c.send(rev_x.encode())
        break

except Exception as e:
    print(e)
    print("something went wrong")
