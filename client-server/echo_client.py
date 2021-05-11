import socket
host = socket.gethostname()
port = 9999

s = socket.socket()

s.connect((host, port))

s.sendall("This will be sent to my server".encode("ascii"))

data = s.recv(1024)

print(data)
s.close
