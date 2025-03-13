import socket
import sys
from datetime import datetime
import argparse

# CMD Arguement Parser
def main():
    
    parser = argparse.ArgumentParser(description="Port Scanner")
    group = parser.add_mutually_exclusive_group()
    parser.add_argument("host", help="Target host IP to scan")
    group.add_argument("-p", "--port", type=int, default=0, help="Scan single port")
    group.add_argument("-r", "--range", default='', help="Scan range of ports(e.g. 30-50)")
    args = parser.parse_args()

    host = str(args.host)
    port = int(args.port)
    port_range = str(args.range)
    
    if port != 0:
        scan_single_port(host, port)
        
    elif port_range != '':
        
        if '-' in port_range:
            port_start, port_end = map(int, port_range.split("-"))
            scan_port_range(host, port_start, port_end)
    
    else:
        pass
    
    
# Scan port status
def scan_port(host, port):
    try:
        # Create socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1) # set timeout for connection to ip so wont loop infinitely

        # Attempt a network connection
        conn = sock.connect_ex((host, port))
        
        if conn == 0:
            print("[ " + str(datetime.now().strftime("%x %X")) + " ] " + f"Port {port}: OPEN")
        else:
            print("[ " + str(datetime.now().strftime("%x %X")) + " ] " + f"Port {port}: CLOSED")
    
    except:
        print(f"Unable to connect to host {host} on port {port}")
        sys.exit()
    
    finally:
        # Close the socket
        sock.close()
        

# Scan single port
def scan_single_port(host, port):
    print("[ " + str(datetime.now().strftime("%x %X")) + " ] " + f"Scanning port {port} on {host}")
    scan_port(host, port)

# Scan range of ports
def scan_port_range(host, port_start, port_end):
    print("[ " + str(datetime.now().strftime("%x %X")) + " ] " + f"Scanning ports {port_start}..{port_end} on {host}")
    
    for port in range(port_start, port_end+1):
        scan_port(host, port)

if __name__ == "__main__": 
    main()