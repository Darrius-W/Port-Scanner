import socket
import sys

if len(sys.argv) == 4:
    # Accept input with command line args
    host_ip = str(sys.argv[1])
    port_start = int(sys.argv[2])
    port_end = int(sys.argv[3])
else:
    print("Invalid amount of Arguments")
    sys.exit()
    
# Function to scan individual host ports 
def port_scanner(host_ip, port_start, port_end):
    try:
        for port in range(port_start, port_end+1):
            # Create socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1) # set timeout for connection to ip so wont loop infinitely
        
            # Attempt a network connection
            result = sock.connect_ex((host_ip, port))
            
            if result == 0:
                print("Port {} is open".format(port))
            else:
                print("Connection to port {} failed".format(port))
    
    except:
        print("Unable to connect to host {} on port {}".format(host_ip, port))
        sys.exit()
    
    finally:
        # Close the socket
        sock.close()
        
        
port_scanner(host_ip, port_start, port_end)