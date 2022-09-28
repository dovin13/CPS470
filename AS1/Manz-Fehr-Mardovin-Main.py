from AS1socket import TCPsocket
from AS1request import Request
import socket
import time
from urllib.parse import urlparse
import threading
from queue import Queue


threadLock = threading.Lock()
blank = 0
counter = 0

class thread(threading.Thread):

    def __init__(self, thread_ID):
        threading.Thread.__init__(self)
        self.thread_ID = thread_ID
        # helper function to execute the threads
    def run(self):
     
      while Q:
        print(len(Q))
        threadLock.acquire()
        #call to all the logic for the main program 
        thread.Logic(self.thread_ID)
        threadLock.release()
        if(len(Q) == 0):
            thread(self.thread_ID).do_run = False
    def Logic(id):
      #set global here initialization above this class
      global blank
      global counter
      if(len(Q) == 0):
            return ''
      if(id == 0):
        blank = blank + 2
        active = threading.active_count() - 1
        print("time: " + str(blank) + " active: " + str(active))
        time.sleep(2)
        return ''
      else:
       if(len(Q) != 0):
    #Parts that need to be looped (starting point)
    
        mysocket = TCPsocket() # create an object of TCP socket
        mysocket.createSocket()
        host = Q.pop(0)
        print(id)
        counter = counter + 1
        print("counter: " + str(counter))

        parsed = urlparse(host) #parses url to get specific things from the URL itself
        port  = 80
        ip = mysocket.getIP(parsed.hostname)      # ip is a local variable to getIP(hostname), ip is of string type
        if(checkHost.count(parsed.hostname) == 1):
            print('Checking host uniqueness... passed')
        else:
            print('Checking host uniqueness... failed')

   
        if(checkIP.count(ip) == 1 and ip != None):
            print('Checking IP uniqueness... passed')
        else:
            print('Checking IP uniqueness... failed')
        mysocket.connect(ip, port)

        myrequest = Request()
        msg1 = myrequest.getRequest(parsed.hostname, parsed.path, parsed.query)
        mysocket.send(msg1)
        dat = mysocket.receive()
        print('Verifying header... status code ' + str(dat[9: 12].decode()))

        #print('getRequest: ' + dat.decode())
        print('_' *120)
        mysocket.close()
        return ''




def getnewIP(hostname):
        if (len(hostname) > 64):  # socket fails with idna codec error when a host name exceeds 64 characters.
            return None
        try:
            ip = socket.gethostbyname(hostname)   # ip is a local variable to getIP(hostname), ip is of string type
        except socket.gaierror:
            x =1
            return None
        return ip

if __name__ == "__main__":

 #for part 3
 #https://stackoverflow.com/questions/6181935/how-do-you-create-different-variable-names-while-in-a-loop
 #use link above to create multiple threads in a loop after input of how many threads needed

 
 global checkIP
 global checkHost
 global pendingqueue
 global extracted
 global successDNS
 global uniqueIP
 global uniqueHost
 global robotcheck
 global HTTPcode
 
 
 urlArray = []
 HTTPcode = []
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
 thread2 = thread(2)
 thread0 = thread(0)
 thread3 = thread(3)
 thread4 = thread(4)


 thread1.start()
 thread2.start()
 thread0.start()
 thread3.start()
 thread4.start()


 thread1.join()
 thread2.join()
 thread0.join()
 thread3.join()
 thread4.join()


 
 print('hello')





