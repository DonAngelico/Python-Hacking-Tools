import socket
from IPy import IP


class PortScanner:
    def __init__(self, target, port_num):
        self.target = target
        self.port_num = port_num
        self.banners = []
        self.open_ports = []

    def scan(self):
        converted_ip = self.check_ip(self.target)

        for port in range(1, self.port_num + 1):
            self.scan_port(converted_ip, port)

    def check_ip(self, ip):
        try:
            IP(ip)
            return ip
        except ValueError:
            return socket.gethostbyname(ip)

    def scan_port(self, ip, port):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)

            sock.connect((ip, port))
            self.open_ports.append(port)

            try:
                banner = sock.recv(1024).decode().strip('\n').strip('\r')
                self.banners.append(banner)
            except:
                self.banners.append("")

            sock.close()

        except:
            pass