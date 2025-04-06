import socket

def scan_ports(target):
    open_ports = []
    for port in range(1, 1025):  # اسکن پورت‌های ۱ تا ۱۰۲۴
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

if __name__ == '__main__':
    target_ip = input("Enter the IP address to scan: ")
    open_ports = scan_ports(target_ip)
    if open_ports:
        print(f"Open ports on {target_ip}: {open_ports}")
    else:
        print("No open ports found.")
