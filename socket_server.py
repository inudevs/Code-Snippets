import socket

with socket.socket() as sock:
    sock.bind(('localhost', 5000))
    sock.listen()
    conn, _ = sock.accept()
    while True:
        data = conn.recv(1024)
        print(int(data.decode()))
