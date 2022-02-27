# First import the socket library
import socket;
#Create a socket object
s = socket.socket();
print("Socket created");
#Connect to port number
port = 4567;
# Bind to the port
s.bind(("",port));
print("Socket bind to %s" %(port));
# Listen to the port
s.listen(5);
print("Socket is listening...");
# Create a forever loop to listen
while True:
  #Establish a connection with the client
  c, addr = s.accept();
  print("Connection from",addr)
