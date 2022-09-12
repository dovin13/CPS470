
from AS1socket import TCPsocket
from AS1request import Request

import time
from urllib.parse import urlparse


def main(): # function, method are the same


    mysocket = TCPsocket() # create an object of TCP socket
    mysocket.createSocket()
    numThreads = input('How many threads to run: ')
    inputfile = input('What is the input file: ')
    X = addURL(inputfile)
    totalnum = len(X)
    #parsed = urlparse(host) #parses url to get specific things from the URL itself

    #Parts that need to be looped (starting point)
    for i in range(totalnum):
        print("\Number of URLs remaining: ", len(X))
        print('URL: ' + host)
        host = X.pop(0)
        parsed = urlparse(host) #parses url to get specific things from the URL itself
   
 
    port  = 80
    print('Parsing URL... host ' + parsed.path + ', port ' + str(port) + ' request /' + parsed.query)   # ip is a local variable to getIP(hostname), ip is of string type
    start = time.perf_counter()
    ip = mysocket.getIP(host)
    end = time.perf_counter()
    timme = (end-start) * 1000
    timme = int(timme)
    print("Doing DNS... done in ",str(timme)," ms, found ", ip)
    start2 = time.perf_counter() #connection timer 
    mysocket.connect(ip, port)
    timme = (time.perf_counter() - start2) * 1000
    timme = int(timme)
    print('Connecting on page... done in ' + str(timme) + ' ms')

    # build our request
    myrequest = Request()
    msg = myrequest.headRequest(host)
   # print(msg.decode())
   


    # send out request

    mysocket.send(msg)
    start = time.perf_counter()
    data = mysocket.receive() # receive a reply from the server
    end = time.perf_counter()
    tim = (end - start) * 1000
    tim = int(tim)
    print('Loading... done in '+ str(tim) + ' ms'  + ' with ' + str(len(data)) + ' bytes')
    string = data.decode()

    print('Verifying header... status code ' + str(string[9: 12]))
    

    print('_' * 120)
   #where looping needs to end (end point)

    print(data.decode())

    msg1 = myrequest.getRequest(host, parsed.path, parsed.query)
    mysocket.send(msg1)
    dat = mysocket.receive()
    #the get request does not send back info the HEAD request does and logic is up above
    #print('MMM: ' + str(dat))
    mysocket.close()



# call main() method:
if __name__ == "__main__":
   main()