import socket
from termcolor import termcolor

def scan(target, ports):
    print('\n' + 'Starting scan for ' + str(target))
    for port in range(1, ports):
        scan_port(target, port)
def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.connect((ipaddress, port))
        print("[+]Port opened " + str(port))
        sock.close()
    except:
        pass

targets = input("Enter IP address (split with comma): ")
ports = int(input("Enter how many ports to scan: "))
if ',' in targets:
    print(termcolor.colored(("[*]Scanning Multiple Targets..."), 'green'))
    for ip in targets.split(','):
        scan(ip.strip(' '), ports)
else:
    print("[*]Scanning One Target...")
    scan(targets, ports)
print("[*]Exiting Program")