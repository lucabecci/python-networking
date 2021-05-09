import socket 

s = socket.socket()
host = socket.gethostname()
port = 9999

s.bind((host, port))

print("Waiting for connection...")
s.listen(5)

while True:
    conn, addr = s.accept()
    try:
        print("Got connection from:", conn)
        conn.send("Server say hi".encode("ascii"))
    finally:
        conn.close()
