import socket 
host = socket.gethostname()
port = 9999

s = socket.socket()
s.bind((host, port))

s.listen(5)

conn, addr = s.accept()

print("Connected by", addr)

while True:
    data = conn.recv(1024)

    d = data.decode("ascii").split(',')

    data_add = int(d[0]) + int(d[1])

    conn.sendall(str(data_add).encode("ascii"))

conn.close()