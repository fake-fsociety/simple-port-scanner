import socket
import sys
from datetime import datetime

def scan_host(host, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        code = s.connect_ex((host, port))
        s.close()
        if code == 0:
            print("[*] Port %d: Open" % (port))
        else:
            print("[*] Port %d: Closed" % (port))
    except Exception as e:
        pass

print("#"*50)
print("Port Scanner")
print("#"*50)
try:
    host = input("Enter Target Host Address: ")
except KeyboardInterrupt:
    print("\n\n[*] User Requested An Interrupt.")
    print("[*] Application Shutting Down.")
    sys.exit(1)

hostip = socket.gethostbyname(host)
print("\n[*] Host %s IP: %s" % (host, hostip))

print("#"*50)
print("Scanning started")
print("#"*50)

max_port = 5000
min_port = 1

start_time = datetime.now()

for port in range(min_port, max_port):
    print("Scanning port: %d" % (port))
    response = scan_host(host, port)

stop_time = datetime.now()
total_time_duration = stop_time - start_time

print("#"*50)
print("Scanning finished")
print("#"*50)

print("\n[*] Scanning Duration: %s ..." % (total_time_duration))
