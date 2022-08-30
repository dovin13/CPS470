# Authors: A, B, C, D
# Date

"""
https://stackoverflow.com/questions/32062925/python-socket-server-handle-https-request

https://docs.python.org/3/library/ssl.html

import socket, ssl

HOST = "www.youtube.com"
PORT = 443

context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_sock = context.wrap_socket(s, server_hostname=HOST)
s_sock.connect((HOST, 443))
s_sock.send(" GET / HTTP/1.1\r\nHost: www.youtube.com\r\n\r\n ".encode())

while True:
    data = s_sock.recv(2048)
    if ( len(data) < 1 ) :
        break
    print(data)

s_sock.close()
"""


# resources: https://docs.python.org/3/howto/sockets.html

import socket

TIMEOUT = 20 # unit is seconds
BUF_SIZE = 1024 # unit is bytes

class TCPsocket:
    # list our instance variables
    # Constructor: create an object
    def __init__(self):
        self.sock = None  # each object's instance variables
        self.host = ""  # remote server's host name
        #print("create an object of TCPsocket")

    # create a TCP socket
    def createSocket(self):
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # self.sock is an instance variable
           # print("created a TCP socket!")
        except socket.error as e:
           # print("Failed to create a TCP socket {}".format(e))
            self.sock = None

    # given a host name, how to get its ip address
    # Return the ip of input hostname. Both ip and hostname in string
    def getIP(self, hostname):
        self.host = hostname
        if (len(hostname) > 64):  # socket fails with idna codec error when a host name exceeds 64 characters.
            return None
        try:
            ip = socket.gethostbyname(hostname)
        except socket.gaierror:
            print("Failed to gethostbyname")
            return None
        return ip


    # connect to a remote server: IP address (a string), port (integer)
    def connect(self, ip, port):
        if self.sock is None or ip is None:
            self.sock = None  # <-- add this line: to disable the rest of socket function calls. 9-2-2021
            return
        try:
            self.sock.settimeout(TIMEOUT)
            self.sock.connect((ip, port))   # server address is defined by (ip, port)
            print("Successfully connected to host:", ip)
        except socket.error as e:
            print("Failed to connect: {}".format(e)) # if timeout, socket error in receive: timed out
            self.sock.close()
            self.sock = None

    # send request to server. Input request is a string, return the number of bytes sent
    def send(self, request): # request is a bytearray
        bytesSent = 0       # bytesSent is a local variable
        if self.sock is None:
            return 0
        try: # our request is not big, so we can sendall at once
            bytesSent = self.sock.sendall(request) #.encode())   # encode(): convert string to bytes
        except socket.error as e:
        #    print("socket error in send: {}".format(e))
            self.sock.close()
            self.sock = None
        return bytesSent

    # Receive the response from the server. Return the reply as bytearray
    def receive(self) -> bytearray:

        if self.sock is None:
            return b''  # return an empty bytearray, terminate this method
        reply = bytearray()
        bytesRecd = 0   # local variable, integer
        self.sock.settimeout(TIMEOUT) # Sets the socket to timeout after TIMEOUT seconds of no activity
        try:
            while True:     # use a loop to receive receive all data
                data = self.sock.recv(BUF_SIZE)  # returned chunk of data with max length BUF_SIZE. data is in bytes
                if data == b'':  # if empty bytes
                    break
                else:
                    reply += data  # append to reply
                    bytesRecd += len(data)
                    if (bytesRecd > 16000): # bigger than 16K bytes. Do not let remote server overload our RAM
                        break
        except socket.error as e:
            print("socket error in receive: {}".format(e))  # if timeout, socket error in receive: timed out
            self.sock.close()
            self.sock = None
        return reply

    # Close socket
    def close(self):
        if not (self.sock is None):
            self.sock.close()