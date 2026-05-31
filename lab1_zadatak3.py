import socket

ports = [80, 443, 22, 25]

for port in ports:
    service = socket.getservbyport(port)
    print(f"Port {port}: {service}")
