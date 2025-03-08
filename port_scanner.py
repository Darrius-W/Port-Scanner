import socket
import sys

# Accept input with command line args
host_ip = str(sys.argv[1])
port = int(sys.argv[2])

# Function to scan individual host ports 
def port_scanner(host_ip, port):
    try:
        # Create socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1) # set timeout for connection to ip so wont loop infinitely

        # Attempt a network connection
        result = sock.connect_ex((host_ip, port))
        
        if result == 0:
            print("Port {} is open".format(port))
        else:
            print("Connection to port failed")
    
    except:
        print("Unable to connect to host {} on port {}".format(host_ip, port))
        sys.exit()
    
    finally:
        # Close the socket
        sock.close()
        
        
port_scanner(host_ip, port)