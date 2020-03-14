import csv
import socket

s = socket.socket()
server_name = input("Enter server name:")
print("server created by the name:", server_name)
s.bind(("localhost", 9999))
s.listen(100)
flag=0
while True:
    if flag>0:
        print("waiting for next user or other client ")
    flag=flag+1
    c, addr = s.accept()
    print("connection established with  client ")
    username = c.recv(1024).decode()
    print("this server is now connected with user named ", username, )
    c.send(bytes('welcome to my server named %s' % server_name, 'utf-8'))
    password= c.recv(1024).decode()
    print(password)
    file = open("login_credentials.csv", 'r')
    reader = csv.reader(file)
    fl=0
    for line in reader:
        if line[1]==username and line[0]==password :
            c.send(bytes("SUCCESSFUL LOGIN", 'utf-8'))
            fl=1
    if fl==0 :
        c.send(bytes("incorrect username or password", 'utf-8'))
    c.close()
