import socket

ip_address = "8.8.8.8"

try:
    hostname = socket.gethostbyaddr(ip_address)
    print(f"IP adresa: {ip_address}")
    print(f"Hostname: {hostname[0]}")
except socket.herror:
    print("Hostname nije pronađen.")
