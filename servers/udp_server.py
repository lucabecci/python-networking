import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

udp_host = socket.gethostname()
udp_port = 9999

sock.bind((udp_host, udp_port))

while True:
    print("Waiting for client...")
    data, addr = sock.recvfrom(1024)
    print("Received msg:", data, "from:", addr)

