from AS1socket import TCPsocket
from AS1request import Request
import socket
import time
from urllib.parse import urlparse
import threading
from queue import Queue


threadLock = threading.Lock()


class thread(threading.Thread):
    def __init__(self, thread_ID):
        threading.Thread.__init__(self)
        self.thread_ID = thread_ID

        # helper function to execute the threads
    def run(self):
      while Q:
        threadLock.acquire()
        #call to all the logic for the main program 
        thread.Logic()
        threadLock.release()
    def Logic():
      if(len(Q) == 0):
            return ''
      if(len(Q) != 0):
    #Parts that need to be looped (starting point)
        mysocket = TCPsocket() # create an object of TCP socket
        mysocket.createSocket()
        if(len(Q) == 0):
            return ''
        host = Q.pop(0)
        print('URL: ' + host)
        parsed = urlparse(host) #parses url to get specific things from the URL itself
        port  = 80
        print('Parsing URL... host ' + parsed.hostname + ', port ' + str(port) + ' request /' + parsed.query)   
        start = time.perf_counter()
        ip = mysocket.getIP(parsed.hostname)      # ip is a local variable to getIP(hostname), ip is of string type
        if(checkHost.count(parsed.hostname) == 1):
            print('Checking host uniqueness... passed')
        else:
            print('Checking host uniqueness... failed')
        end = time.perf_counter()
        timme = (end-start) * 1000
        timme = int(timme)
        print("Doing DNS... done in ",str(timme)," ms, found ", ip)
        start2 = time.perf_counter() #connection timer 
        if(checkIP.count(ip) == 1 and ip != None):
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
       # print(msg.decode())
    # send out request
        start3 = time.perf_counter()
        mysocket.send(msg)
        end3 = time.perf_counter()
        timee = (end3 - start3) * 1000000
        timee = int(timee)
        print('Connecting on robots... done in ' + str(timee) + ' microsecond')
        start = time.perf_counter()
        data = mysocket.receive()
        end = time.perf_counter()
        tim = (end - start) * 1000
        tim = int(tim)
        print('Loading... done in '+ str(tim) + ' ms'  + ' with ' + str(len(data)) + ' bytes')
        string = data.decode()
        print('Verifying header... status code ' + str(string[9: 12]))
    
        print('_' * 120)

       
        msg1 = myrequest.getRequest(parsed.hostname, parsed.path, parsed.query)
        mysocket.send(msg1)
        dat = mysocket.receive()
    #the get request does not send back info the HEAD request does and logic is up above
       # print('getRequest: ' + dat.decode())
        print('_' *120)
        mysocket.close()
        return ''
   # time.sleep(1)
#end of Logic(met)


def getnewIP(hostname):
        if (len(hostname) > 64):  # socket fails with idna codec error when a host name exceeds 64 characters.
            return None
        try:
            ip = socket.gethostbyname(hostname)   # ip is a local variable to getIP(hostname), ip is of string type
        except socket.gaierror:
            x =1
            return None
        return ip
#main Method
if __name__ == "__main__":

 #for part 3
 #https://stackoverflow.com/questions/6181935/how-do-you-create-different-variable-names-while-in-a-loop
 #use link above to create multiple threads in a loop after input of how many threads needed

 urlArray = []
 global checkIP
 global checkHost
 checkIP = []
 checkHost = []
 
 with open("URL-input-100.txt", "r") as d:

    for lines in d:
        mysocket = TCPsocket() # create an object of TCP socket
        mysocket.createSocketnoPrint()
        parse = urlparse(lines)
        ips = getnewIP(parse.hostname)
        checkIP.append(ips)
        checkHost.append(parse.hostname)
        urlArray.append(lines)
        mysocket.close()
    #the txt file is put inside a queue then change logic to pop Q instead of a for loop
    Q = Queue()
    Q = urlArray
 s = ''.join(urlArray)
 print('Opened URL-input.txt with size ' + str(len(s)) + ' bytes')



 thread1 = thread(1)
 thread1.start()
 thread1.join()





