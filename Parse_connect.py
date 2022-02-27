import socket
import sys
import argparse
# Define previous lab as a function - ploadconnect() with 2 options hostname and port
def ploadconnect(websiteN, portN):
    try:
       #Where AF_INET specify IPv4
       s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       print("Socket created successfully")
    except socket.error as err:
        print("Socket creation failed with error %s" %(err))
    # Default web port
    port = portN
    try:
        host_ip = socket.gethostbyname(websiteN)
    except socket.gaierror:
        print("There is a problem resolving the host")
        sys.exit()
    # Connect to the web server
    s.connect((host_ip,port));
    print("Successfully connected to the website given %s:%s" %(host_ip, port));
    # End of function
parser = argparse.ArgumentParser(description="Learn to connect to a website with port number");
parser.add_argument("-H", "--host", required=True, help="specify the hostname or website name");
parser.add_argument("-p", "--port", type=int, default=80, help="specify the port number eg. 80 for website");


args = parser.parse_args();
ploadconnect(args.host,args.port);
