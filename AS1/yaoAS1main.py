
from yaoAS1socket import TCPsocket
from yaoAS1request import Request
import sys
import time
from urllib.parse import urlparse

def main(): # function, method are the same


    mysocket = TCPsocket() # create an object of TCP socket
    mysocket.createSocket()
    host = sys.argv[1]
    parsed = urlparse(host) #parses url to get specific things from the URL itself
    print(parsed)
    print('URL: ' + host)
   
    ip = mysocket.getIP(host)
 
    port  = 80
    print('Parsing URL... host ' + parsed.path + ', port ' + str(port) + ' request /' + parsed.query)   # ip is a local variable to getIP(hostname), ip is of string type

    start2 = time.perf_counter() #connection timer 
    mysocket.connect(ip, port)
    print('Connection on page took: ' + str(time.perf_counter()-start2) + ' seconds')

    # build our request
    myrequest = Request()
    msg = myrequest.headRequest(host)
    print(msg.decode())

    # send out request
    mysocket.send(msg)
    data = mysocket.receive() # receive a reply from the server
    print('_' * 120)
    print(data.decode())
    mysocket.close()

# call main() method:
if __name__ == "__main__":
   main()