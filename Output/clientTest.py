'''
Created on Oct 8, 2017

@author: bebop
'''

import socket, pickle

host = socket.gethostname()
port = 4500
if __name__ == '__main__':
    try:
            
        client = socket.socket()
        client.connect((host, port))
        while(True):
            print("Getting data")
            print(pickle.loads(client.recv(72)))

    finally:
        print("Closing Client")
        client.close()    
    pass