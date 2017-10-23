
import Analysis.Analysis as an
import Output.Output as out
import NeuralNetwork.NNModule as nn
import Camera.Camera as cam
#import Debug.Debug as deb
import sys

debug = False

if __name__ == '__main__':
    if(len(sys.argv) > 1):
        if(str.lower(sys.argv[1]) == "debug"):
            print("--Setting mode to Debug--")
            debug = True
     
    if(debug):
        an.debug()
        print("Initializing cam")
    cam.init("video.mp4")
    
    if(debug):
        print("Initializing NeuralNetwork")
    nn.__init
#    out.init()
#    if(debug):
#        deb.init()
    
    while(True):
#        try:
        if(debug):
            print("Getting frame from cam")
        frame = cam.get_image()
        
        if(debug):
            print("Getting List from Network")
        data = nn.analyze(frame)
        
        if(debug):
            print("Getting result from analysis")
        result = an.getData(data)
        
        if(debug):
            print("--Printing Results--")
            print(result)

        if(debug):
            print("--------------------")
            
#        if(debug):
#           deb.printToTerm(result)
#           deb.updateImage(frame)
#           deb.updateNetText(list)
#           deb.updateResText(result)
                
#        finally:
#            out.close()

