
from AS1socket import TCPsocket
from AS1request import Request
import socket
import time
from urllib.parse import urlparse



def getnewIP(hostname):
        
        if (len(hostname) > 64):  # socket fails with idna codec error when a host name exceeds 64 characters.
            return None
        try:
            ip = socket.gethostbyname(hostname)   # ip is a local variable to getIP(hostname), ip is of string type
        except socket.gaierror:
            print("Failed to gethostbyname")
            return None
        return ip

def main(): # function, method are the same



 #numThreads = input('How many threads to run: ')
 #inputfile = input('What is the input file: ')

 checkIP = []
 checkHost = []
 with open("URL-input-100.txt","r") as f:
  
  for line in f:
    #Parts that need to be looped (starting point)
    mysocket = TCPsocket() # create an object of TCP socket
    mysocket.createSocket()
    host = line
    print('URL: ' + host)
    parsed = urlparse(host) #parses url to get specific things from the URL itself
   
 
    port  = 80
    print('Parsing URL... host ' + parsed.hostname + ', port ' + str(port) + ' request /' + parsed.query)   
    start = time.perf_counter()


    ip = mysocket.getIP(parsed.hostname)      # ip is a local variable to getIP(hostname), ip is of string type

    checkHost.append(parsed.hostname)
    checkIP.append(ip)


    if(checkHost.count(parsed.hostname) == 1):
        print('Checking host uniqueness... passed')
    else:
        print('Checking host uniqueness... failed')
    end = time.perf_counter()
    timme = (end-start) * 1000
    timme = int(timme)
    print("Doing DNS... done in ",str(timme)," ms, found ", ip)
    start2 = time.perf_counter() #connection timer 
    if(checkIP.count(ip) == 1):
        print('Checking IP uniqueness... passed')
    else:
        print('Checking IP uniqueness... failed')
    mysocket.connect(ip, port)
    timme = (time.perf_counter() - start2) * 1000
    timme = int(timme)
    print('Connecting on page... done in ' + str(timme) + ' ms')

    # build our request
    myrequest = Request()
    #working on what is passed into this
    msg = myrequest.headRequest(parsed.hostname)
    print(msg.decode())
    # send out request
    mysocket.send(msg)
    start = time.perf_counter()
    data = mysocket.receive()
    end = time.perf_counter()
    tim = (end - start) * 1000
    tim = int(tim)
    print('Loading... done in '+ str(tim) + ' ms'  + ' with ' + str(len(data)) + ' bytes')
    string = data.decode()
    print('Verifying header... status code ' + str(string[9: 12]))
    
    print('_' * 120)

    print(data.decode())
    msg1 = myrequest.getRequest(parsed.hostname, parsed.path, parsed.query)
    mysocket.send(msg1)
    dat = mysocket.receive()
    #the get request does not send back info the HEAD request does and logic is up above
    #print('getRequest: ' + dat.decode())
    print('_' *120)
    mysocket.close()
    time.sleep(1)



# call main() method:
if __name__ == "__main__":
   main()