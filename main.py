
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
datachanged = 0
numCamIter = 0
numNNIter = 0

#a thread lock for entering and exiting the frame's critical region
frameLock = threading.Lock()

#a thread lock for entering and exiting the data's critical region
dataLock = threading.Lock()

#class for running the cam thread
class camThread(threading.Thread):
    def run(self):
        while(True):
            global frameLock, sharedFrame, debug, numCamIter
            #Always want the camera to be running and getting new frames
            #frame = cam.get_image()
            
            #print("Cam: Attempting framelock")
            # along the frame only when able
            if(frameLock.acquire(0)):
                #if(debug):
                    #print("Cam: Updating frame")
                numCamIter += 1
                print("Cam: ", numCamIter)
                #frame = cam.get_image()
                cam.get_image()
                #sharedFrame = frame
                #if(debug):
                #    print("Checking shared frame")
                #    print(sharedFrame)
                frameLock.release()
                time.sleep(.5)
                #print("Cam: framelock released")

#class for running the neural network thread
class nnThread(threading.Thread):    
    #TODO Currently, it is possible to analyze the same frame multiple times
    #A possible solution is to make the sharedFrame = None after analysis, but
    #that runs the risk of ignoring frames since cam is asynchronous
    def run(self):
        global frameLock, dataLock, sharedData, sharedFrame, debug, datachanged, numNNIter
        while(True):
            #print("Start of NNT")
                        
            if(debug):
                print("NN: frameLock grab")
                print(frameLock)
            #blocks the thread until a frame can be acquired
            frameLock.acquire(1)
            #localFrame = sharedFrame
            localData = None
            try:
                numNNIter += 1
                print("NN: ", numNNIter)
                if(debug):
                    print("Beginning analysis")
                localData = nn.analyze_image("Camera/img.jpg")
                print("Data from analysis")
                print(localData)
            except:
                print("Image not found")
            #if(debug):
            #    print(localFrame)
            frameLock.release()
            if(debug):
                print("NN: frameLock released")
                print(frameLock)
            #if(localFrame != None):
            #   if(debug):
            #       print("NN: Analyzing")
            #        print(localFrame)
                #localData = nn.analyze_image("/media/img.jpg")
            
            if(debug):
                print("NN: datalock grab")
            #forces the neural network to wait until it can  along its most recent results
            dataLock.acquire(1)
            if(debug):
                print("NN: Updating data")
            sharedData = localData
            datachanged = 1
            dataLock.release()
            if(debug):
                print("NN: datalock release")
            #else:
            #    time.sleep(2)

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
    while(True):
        olddata = None

        if(not ct.is_alive):
            print("CT Stopped Running")
            sys.exit()

        if(not nnt.is_alive):
            print("NNT Stopped Running")
            sys.exit()

        #blocks until it can acquire data to be further analyzed
        dataLock.acquire(1)
        data = sharedData
        #if(debug):
        if(datachanged == 1):
            print("Acquired data")
            print(data)
            datachanged = 0
            print("--------------------")
        dataLock.release()
        olddata = data
        
        #if(data != None):
        #    if(debug):
        #        print("Getting result from analysis")
        #    result = an.getData(data)
        #    if(debug):
        #        print("--Printing Results--")
        #        print(result)
        
        #TODO Need to output the results now
        
        #if(debug):
        #    print("--------------------")
            
            
        count += 1
            
#        if(debug):
#           deb.printToTerm(result)
#           deb.updateImage(frame)
#           deb.updateNetText(list)
#           deb.updateResText(result)
                
#        finally:
#            out.close()
