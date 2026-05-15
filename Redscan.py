#!/bin/env python3

import socket
import subprocess
import sys
import time

print("[+] welcome to RedScan")
time.sleep(1)
ip = input("[+] Target IP:")
start_port = 1
end_port = 65535
print(f"[+] scanning {ip}")


def ip_valid(ip):
    command = ["ping", "-w", "1", ip]
    runcmd = subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if runcmd.returncode == 0:
        print("[+] host is up")
    else:
        print("[-] host is down")
        sys.exit()


print(ip_valid(ip))


def scan_ip(ip, start_port, end_port):
    for port in range(start_port, end_port):
        declare = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        declare.settimeout(0.5)
        is_open = declare.connect_ex((ip, port))
        if is_open == 0:
            print(f"[+] port {port} is open")
        declare.close()


scan_ip(ip, start_port, end_port)

