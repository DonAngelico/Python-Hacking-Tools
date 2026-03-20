import portscanner

targets_ip = input('[+] Enter the target IP address: ')

port_number = int(input(
    '[+] Enter the Amount of Ports You Wish to Scan '
    '[500 - Scan First 500 ports, 1000 - Scan First 1000 ports, 65535 - Scan All Ports]: '
))
vul_file = input('[+] Enter the name of the file containing the list of vulnerabilities (e.g., vulns.txt): ')
print('\n')
target = Portscanner.PortScan(targets_ip, port_number)
target.scan()

with open(vul_file, 'r') as file:
    count = 0

    for banner in target.banners:

        file.seek(0)

        for line in file.readlines():
            if line.strip() in banner:
                print(f'[!] Vulnerability Found: "{banner}" on port {target.open_ports[count]}')

        count += 1