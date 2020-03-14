import socket

cname = input("Enter the client name:")
c = socket.socket()

print("client created with name:", cname)
# ip=input("enter name or ip of the server ")
# port=int(input("enter the port number you want to connect:")
# c.connect((ip,port))
c.connect(("localhost", 9999))
print("connection established with server.")
username = input("Welecome user.please enter your username:")

c.send(bytes(username, 'utf-8 '))
msg = c.recv(1024).decode()
print("the following acknowledgement was received from server:\n", msg)
password=input("Enter PASSWORD:")
c.send(bytes(password, 'utf-8 '))
sf = c.recv(1024).decode()
print(sf)
