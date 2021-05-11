import socket
host = socket.gethostname()
port = 9999

a = str(input("Enter the first number:"))
b = str(input("Enter the second number:"))

result = a + ',' + b

print("Sending string {0} to server".format(result))

s = socket.socket()
s.connect((host, port))

s.sendall(result.encode('ascii'))

data = s.recv(1024)
print(int(data.decode("ascii")))

s.close()