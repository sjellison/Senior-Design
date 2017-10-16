
import socket, pickle
import atexit

host = "tx1-dec1710.student.iastate.edu"
#host = socket.gethostname()
port = 4500

server = socket.socket()
conn = socket.socket()

def init():
    global conn
    global server
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(1)
    
    print("Server waiting for client...")
    conn, client_addr = server.accept()  #returns a connection and an address to the client that connected
    print("Connected to ", client_addr)
    #print("Test completed, closing socket")
    #server.close()

def out(data=[]):
    global conn
    dataArr = parse(data)
    print("Sending data...")
    print("Sending ", dataArr.__sizeof__(), "bytes")
    if(not(conn.send(pickle.dumps(dataArr)))):
        print("Errror during server send")

def close():
    global conn
    global server
    conn.close()
    server.close()
            
'''
This is a very strict parsing of the data. This is being parsed
with strict knowledge of the data input and that is a bad way
to do it. This needs to change
'''      
def parse(data={}):
    dat = 0
    arrPos = 0
    ret = []
    for _ in data:
        if(_ == 'xposition'):
            dat = 1
        elif(_ == 'yposition'):
            dat = 2
        elif(_ == 'distance'):
            dat = 3
            
        elif(dat == 1):
            ret.append(_)
            arrPos += 1
        elif(dat == 2):
            ret.append(_)
            arrPos += 1
        elif(dat == 3):
            ret.append(_)
            arrPos += 1
            dat = 0
            
        else:
            ret.append(_)
            arrPos += 1
        
    return ret
        
        
        
        