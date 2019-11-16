
import socket

try:
    socket_obj = socket.socket()
    print("socket created succesfully")

    port = 80

    socket_obj.bind(('', port))
    socket_obj.listen(5)

    while True:
        c, address = socket_obj.accept()
        c.send(b"Thanks for connecting")
        c.close()

except Exception as e:
    print(e)
    print("something went wrong")
