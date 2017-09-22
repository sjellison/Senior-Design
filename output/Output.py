'''
Created on Sep 6, 2017

@author: Sean Jellison
'''

#import bluetooth
import serial

def outputData(data):
    for _ in data:
        print(_)

'''
port = None
def usart_init():
    #need to figure out all these parts
    port = serial.Serial("port", baudrate=, timeout=1.0, parity=, stopbits=, bytesize)
    
def usart_write(data):
    if(port == None):
        print ("ERROR: port not initialized")
        return

    port.write(data) #writes 1 character at a time
'''
'''      
def bluetooth_init():
    serverMACAddress = '' #tbd
    port = 3
    sock = socket.socket(socket.AF_BLUETOOTH, sock.SOCK_STREAM, socket.BTPRO)
'''