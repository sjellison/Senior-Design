
#import Analysis.Analysis as an
import Output.Output as out
import NeuralNetwork.NNModule as nn
import Camera.Camera as cam
import threading
import time
#import Debug.Debug as deb
import sys


debug = False

sharedFrame = None
sharedData = None

#a thread lock for entering and exiting the frame's critical region
frameLock = threading.Lock()

#a thread lock for entering and exiting the data's critical region
dataLock = threading.Lock()

#class for running the cam thread
class camThread(threading.Thread):
    def run(self):
        while(True):
            global frameLock, sharedFrame, debug
            #Always want the camera to be running and getting new frames
            frame = cam.get_image()
            
            #pass along the frame only when able
            if(frameLock.acquire(0)):
                if(debug):
                    print("Cam: Updating frame")
                    print(frame)
                sharedFrame = frame
                if(debug):
                    print("Checking shared frame")
                    print(sharedFrame)
                frameLock.release()

#class for running the neural network thread
class nnThread(threading.Thread):    
    #TODO Currently, it is possible to analyze the same frame multiple times
    #A possible solution is to make the sharedFrame = None after analysis, but
    #that runs the risk of ignoring frames since cam is asynchronous
    def run(self):
        global frameLock, dataLock, sharedData, sharedFrame, debug
        while(True):
            #blocks the thread until a frame can be acquired
            frameLock.acquire(1)
            if(debug):
                print("NN: Grabbing frame")
            localFrame = sharedFrame
            if(debug):
                print(localFrame)
            frameLock.release()
            
            if(localFrame != None):
                if(debug):
                    print("NN: Analyzing")
                localData = nn.analyze(localFrame)
            
                #forces the neural network to wait until it can pass along its most recent results
                dataLock.acquire(1)
                if(debug):
                    print("NN: Updating data")
                sharedData = localData
                dataLock.release()
            else:
                time.sleep(2)

if __name__ == '__main__':
    #check for debug mode
    if(len(sys.argv) > 1):
        if(str.lower(sys.argv[1]) == "debug"):
            print("--Setting mode to Debug--")
            debug = True
     
    if(debug):
        #an.debug()
        print("Initializing cam")
    cam.init("Camera/video.mp4")
    
    if(debug):
        print("Initializing Cam Thread")
    ct = camThread()
    
    if(debug):
        print("Initializing NeuralNetwork")
    nn.__init__()
    
    if(debug):
        print("Initializing NN Thread")
    nnt = nnThread()
    
    if(debug):
        print("Starting threads")
    try:
        ct.start()
        nnt.start()
    except:
        print("Error starting threads")
        
#    out.init()
#    if(debug):
#        deb.init()
    
    count = 0
    while(count < 10):

        if(debug):
            if(ct.is_alive()):
                print("CT still running")
            else:
                print("CT not running")
            if(nnt.is_alive()):
                print("NNT still running")
            else:
                print("NNT not running")
        #blocks until it can acquire data to be further analyzed
        dataLock.acquire(1)
        data = sharedData
        if(debug):
            print("Acquired data")
            print(data)
        dataLock.release()
        
        #if(data != None):
        #    if(debug):
        #        print("Getting result from analysis")
        #    result = an.getData(data)
        #    if(debug):
        #        print("--Printing Results--")
        #        print(result)
        
        #TODO Need to output the results now
        
        if(debug):
            print("--------------------")
            
        count += 1
            
#        if(debug):
#           deb.printToTerm(result)
#           deb.updateImage(frame)
#           deb.updateNetText(list)
#           deb.updateResText(result)
                
#        finally:
#            out.close()

#Function for the camera thread to run
#def camThread():
#    global frameLock, sharedFrame
#    #TODO needs to pull frames
#    while(True):
#        #Always want the camera to be running and getting new frames
#        frame = cam.getFrame()
#        
#        #pass along the frame only when able
#        if(frameLock.acquire(0)):
#            sharedFrame = frame
#            frameLock.release()
            

#def nnThread():
#    global frameLock, dataLock, sharedData, sharedFrame
#    #TODO needs to analyze frames and spit out results
#    while(True):
#        #blocks the thread until a frame can be acquired
#        frameLock.acquire(1)
#        localFrame = sharedFrame
#        frameLock.release()
#        
#        localData = nn.analyze(localFrame)
#        
#        #forces the neural network to wait until it can pass along its most recent results
#        dataLock.acquire(1)
#        sharedData = localData
#        dataLock.release()
