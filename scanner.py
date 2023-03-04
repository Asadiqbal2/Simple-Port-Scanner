import socket
import sys
from datetime import datetime

# Define our target
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) #Translate Hostname to IPv4
else:
    print("Invalid amount of arguments")
    print("Syntax: python3 scanner.py <IP>")
    sys.exit()

# Add a banner
print('-' * 50)
print("Scanning Started: "+target)
print("Time Started: "+str(datetime.now()))
print("Made By Asad Iqbal")
print('-' * 50)

try:
    for port in range(50,1000):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port)) #returns an error indicator
        if result == 0:
            print("Port is open: {}".format(port))
        s.close()

except KeyboardInterrupt:
    print("\nExiting program")
    sys.exit()

except socket.gaierror:
    print("\nHostname could not be resolved")
    sys.exit()

except socket.error:
    print("\nCouldn't connect to server")
    sys.exit()
