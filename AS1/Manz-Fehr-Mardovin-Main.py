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
hostcounter = 0
ipunique = 0
httpcode = []
httpcodecounter = 0
robot = 0
link = 0


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
        if(len(Q) == 0):
            print('hello')
            thread(self.thread_ID).do_run = False
    def Logic(id):
      #set global here initialization above this class
      global blank
      global counter
      global httpcode
      global httpcodecounter
      global hostcounter
      global ipunique
      global robot
      global link

      if(len(Q) == 0):
            return ''
      if(id == 0):
        blank = blank + 2
        active = threading.active_count() - 1
        print("[ " + str(blank) + "]   " + str(active) + " Q   " + str(len(Q)) + " E   " + str(hostcounter) + " H   " + str(ipunique) + " I   " + " R   " + str(httpcodecounter) + " C   " + " L   " + str(link) +  "K")
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
            hostcounter = hostcounter + 1
            print('Checking host uniqueness... passed')
        else:
            print('Checking host uniqueness... failed')

   
        if(checkIP.count(ip) == 1 and ip != None):
            ipunique = ipunique + 1
            print('Checking IP uniqueness... passed')
        else:
            print('Checking IP uniqueness... failed')
        mysocket.connect(ip, port)

        myrequest = Request()
        msg1 = myrequest.getRequest(parsed.hostname, parsed.path, parsed.query)
        mysocket.send(msg1)
        dat = mysocket.receive()
        data = dat.decode()
        if('robot' in data):
            robot = robot + 1
        link = link + data.count('href')
        httpcode.append(dat[9:12].decode())
        for code in httpcode:
            if(len(code) != 0):
                httpcodecounter = httpcodecounter + 1

        print('Verifying header... status code ' + str(dat[9: 12].decode()))
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
 start = time.perf_counter()
 #for part 3
 #https://stackoverflow.com/questions/6181935/how-do-you-create-different-variable-names-while-in-a-loop
 #use link above to create multiple threads in a loop after input of how many threads needed

 
 global checkIP
 global checkHost
 global robotcheck

 code2 = 0
 code3 = 0
 code4 = 0
 code5 = 0
 codeother = 0
 
 urlArray = []

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


 end = time.perf_counter()

 print("Extracted " + str(counter) + " URLs @ " + str(counter / (end - start)) + "/s")
 print("Looked up " + str(ipunique) + " DNS names @ " + str(ipunique / (end - start)) + "/s")
 print("Downloaded " + str(robot) + " robots @ " + str(robot / (end - start)))
 print("Crawled " + " pages @ ")
 print("Parsed " +  " links @ " + str(0 / (end - start)) + "/s")
 for codes in httpcode:
  if(codes != ''):
    if(codes[0] == '2'):
        code2 = code2 + 1
    if(codes[0] == '3'):
        code3 = code3 + 1
    if(codes[0] == '4'):
        code4 = code4 + 1
    if(codes[0] == '5'):
        code5 = code5 + 1
  if(codes == ''):
    codeother = codeother + 1

 
 print('HTTP codes: 2xx = ' + str(code2) + ", 3xx = " + str(code3) + ", 4xx = " + str(code4) + ", 5xx = " + str(code5) + ", other = " + str(codeother))





