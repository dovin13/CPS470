
from yaoAS1socket import TCPsocket
from yaoAS1request import Request
import sys

def main(): # function, method are the same

    mysocket = TCPsocket() # create an object of TCP socket
    mysocket.createSocket()
    host = sys.argv[1]
   # host = "www.google.com"
    ip = mysocket.getIP(host)
    port  = 80
    mysocket.connect(ip, port)

    # build our request
    myrequest = Request()
    msg = myrequest.headRequest(host)

    # send out request
    mysocket.send(msg)
    data = mysocket.receive() # receive a reply from the server
    print("data received: ", data)

    mysocket.close()

# call main() method:
if __name__ == "__main__":
   main()