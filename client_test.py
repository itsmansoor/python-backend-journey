import socket

client = socket.socket()

client.connect(("localhost", 9999))

message = "Hello Server"
client.send(message.encode())

client.close()