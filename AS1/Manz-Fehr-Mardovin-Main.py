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
        thread.Logic(self.thread_ID)
        threadLock.release()
    def Logic(id):
      if(len(Q) == 0):
            return ''
      if(len(Q) != 0):
    #Parts that need to be looped (starting point)
       if(id == 0):
        print('hello')
       else:
        mysocket = TCPsocket() # create an object of TCP socket
        mysocket.createSocket()
        if(len(Q) == 0):
            return ''
        host = Q.pop(0)
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
       # msg = myrequest.headRequest(parsed.hostname)
       # print(msg.decode())
    
        #mysocket.send(msg)

 

       # data = mysocket.receive()

       # print('Loading... done in '+ str(tim) + ' ms'  + ' with ' + str(len(data)) + ' bytes')
       # string = data.decode()
        #print('Verifying header... status code ' + str(string[9: 12]))
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


 thread0 = thread(0)
 thread1 = thread(1)
 thread2 = thread(2)
 thread3 = thread(3)

 thread0.start()
 thread1.start()
 thread2.start()
 thread3.start()

 thread0.join()
 thread1.join()
 thread2.join()
 thread3.join()
 print('hello')





