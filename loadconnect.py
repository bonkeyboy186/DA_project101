# First import the socket and sys library
import socket
import sys
try:
   #Where AF_INET specify IPv4
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
   print("Socket created successfully");

except socket.error as err:
    print("Socket creation failed with error %s" %(err));

# Default web port
port = 80;
try:
    host_ip = socket.gethostbyname("http://192.168.142.244/freebix"); # Use your IP
except socket.gaierror:
    print("There is a problem resolving the host");
    sys.exit();
# Connect to the web server
s.connect((host_ip,port));
print("Successfully connected to the website given %s:%s" %(host_ip, port));
print("OK");

