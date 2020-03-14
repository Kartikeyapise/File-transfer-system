import socket
import sys

ip = input('Enter hostname of server : ')
port = input('Enter Port : ')
welcome_msg = ('-'*20) + 'WELCOME!' + ('-'*20)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client_socket.connect((ip, int(port)))
    print('Connection Successful!\n')
    print(welcome_msg)
except Exception as e:
    print('Connection Error! due to exception:', e)
    sys.exit()
finally:
    print("")
username = input("please enter username")
client_socket.send(bytes(username, 'utf-8 '))
msg = client_socket.recv(1024).decode()
print("message/acknowledgement from server \n", msg)
password =input("Enter PASSWORD:")
client_socket.send(password.encode())
meg2 = client_socket.recv(1024).decode()
print("finally the message received from server:", meg2)