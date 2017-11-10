
import socket, pickle

host = socket.gethostname()
#host = "tx1-dec1710.student.iastate.edu"
print(host)
port = 4500
if __name__ == '__main__':
    try:
            
        client = socket.socket()
        client.connect((host, port))
        bytesRec = 0
        msglen = 0
        count = 0
        while(count < 100):
            #start of the message, want to figure out how much more is going to be sent
            #if(msglen == 0):
            #    recv = client.recv(8)
            #    print("First recieve result: " + str(recv))
            print("Getting data")
            recv = client.recv(1024)
            print(recv)
            print(pickle.loads(recv), " : ", count)
            count = count + 1

    finally:
        print("Closing Client")
        client.close()    
    pass