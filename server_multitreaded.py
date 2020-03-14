import csv
import socket
from threading import Thread

class ServerThread(Thread):
    def __init__(self, c):
        Thread.__init__(self)
        self. c_socket = c

    def run(self):
        username = self. c_socket.recv(1024).decode()
        print("connection established with client:", username )
        self. c_socket.send(bytes('Welcome CLIENT', 'utf-8'))
        p_d = self. c_socket.recv(1024).decode()
        file = open("login_credentials.csv", 'r')
        reader = csv.reader(file)
        flag= 0
        for line in reader:
            if line[1] == p_d and line[0] == username :
                self. c_socket.send(bytes("SUCCESS", 'utf-8'))
                flag = 1
        if flag == 0:
            self. c_socket.send(b'FAILURE')
        self. c_socket.close()

host = socket.gethostname()
port = input('Enter Port : ')
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    server_socket.bind((host, int(port)))
except:
    print("Bind Failed! Error : " + str(sys.exc_info()))
    sys.exit()

server_socket.listen(5)
print("Hostname : " + host)
print('Socket is now listening...')
print('*' * 40)



while True:
    c_socket, address = server_socket.accept()
    print("connection established with  client ", address)
    thread__ = ServerThread(c_socket)
    thread__.start()

