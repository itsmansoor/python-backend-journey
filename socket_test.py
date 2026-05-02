import socket

s = socket.socket()
s.bind(("localhost",9999))
s.listen(3)
print('waiting for connecction....')

conn,addr = s.accept()

print("Connected with", addr)
data = conn.recv(1024)
print("Client says:", data.decode())