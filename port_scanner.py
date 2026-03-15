import socket

target = input("Enter the IP address to scan: ")

print(f"Scanning target {target}")

scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

for port in range(20,101):
    result = scanner.connect_ex((target, port))
    
    if result == 0:
        print(f"Port {port} is OPEN")

scanner.close()