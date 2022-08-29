
from yaoAS1socket import TCPsocket
from yaoAS1request import Request
import sys
from datetime import date
import datetime
import calendar

def main(): # function, method are the same
    curr_date = date.today()
    current_time = datetime.datetime.now()

    mysocket = TCPsocket() # create an object of TCP socket
    mysocket.createSocket()
    host = sys.argv[1]
    ip = mysocket.getIP(host)
    port  = 80
    mysocket.connect(ip, port)

    # build our request
    myrequest = Request()
    msg = myrequest.headRequest(host)

    # send out request
    mysocket.send(msg)
    data = mysocket.receive() # receive a reply from the server
   
    print("data received: ", data.decode())
   # print(calendar.day_name[curr_date.weekday()] + ', ' + str(current_time.day) + ' ' + current_time.strftime("%b") + ' ' + str(current_time.year) + ' ' + current_time.strftime("%H:%M:%S"))

    mysocket.close()

# call main() method:
if __name__ == "__main__":
   main()