
#import Analysis.Analysis as an
import Output.Output as out
import NeuralNetwork.NNModule as nn
import Camera.Camera as cam
#import Analysis.Analysis as an #not currently used
import threading
import time
import Debug.Debug as deb
import sys


debug = False
demo = False
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

            if(frameLock.acquire(0)):
                numCamIter += 1
                print("Cam: ", numCamIter)

                cam.get_image("Camera/img.jpg")

                frameLock.release()
                time.sleep(.00001)

#class for running the neural network thread
class nnThread(threading.Thread):    
    def run(self):
        global frameLock, dataLock, sharedData, sharedFrame, debug, datachanged, numNNIter
        while(True):
            #print("Start of NNT")
            timeStart = time.time()
            if(debug):
                print("NN: frameLock grab")
                print(frameLock)
            #blocks the thread until a frame can be acquired
            frameLock.acquire(1)
            localData = None
            try:
                numNNIter += 1
                print("NN: ", numNNIter)
                if(debug):
                    print("Beginning analysis")
                localData = nn.analyze_image("Camera/img.jpg")
                #print("Data from analysis")
                #print(localData)
            except:
                print("Image not found")

            frameLock.release()
                
            #forces the neural network to wait until it can  along its most recent results
            dataLock.acquire(1)
            if(debug):
                print("NN: Updating data")
            sharedData = localData
            datachanged = 1
            dataLock.release()
            if(debug):
                print("NN: datalock release")
                
            timeEnd = time.time()
            
            print("Time taken for analysis: "+ str(timeEnd - timeStart))

'''
Main Thread
'''
if __name__ == '__main__':
    #check for debug mode
    if(len(sys.argv) > 1):
        if(str.lower(sys.argv[1]) == "debug"):
            print("--Setting mode to Debug--")
            debug = True
        elif(str.lower(sys.argv[1]) == "demo"):
            demo = True
    
    if(demo):
        print("Demo mode activated. Attempting to initialize demo window...")
        try:
            deb.init()
            demoInit = True
            print("Demo window activated")
        except:
            print("Failed to initialize demo window")
            demo = False
            
    if(debug):
        print("Initializing NeuralNetwork")
    nn.__init__()
    
    if(debug):
        print("Initializing NN Thread")
    nnt = nnThread()
       
    if(debug):
        print("Initializing cam")
    cam.init("Camera/drone_footage.mp4")
    #cam.init("Camera/video.mp4")
    
    if(debug):
        print("Initializing Cam Thread")
    ct = camThread()

    if(debug):
        print("Starting threads")
    try:
        ct.start()
        nnt.start()
    except:
        print("Error starting threads")
        
#    out.init()
    if(debug):
        deb.init()
    
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
            #print("Acquired data")
            #print(data)
            datachanged = 0
            if(demo):
                deb.updateImage(deb.strtoimg("Camera/img.jpg"))
                deb.updateNetText(data)
                deb.updateWindow()
            #print("--------------------")
        dataLock.release()
        olddata = data
        
        #TODO Need to output the results now
            
        count += 1
                
#        finally:
#            out.close()
