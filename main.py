
import Analysis.Analysis as an
import Output.Output as out
import Network.Network as net
import Camera.Camera as cam
import Debug.Debug as deb
import sys

debug = False

if __name__ == '__main__':
    if(len(sys.argv) > 1):
        if(str.lower(sys.argv[1]) == "debug"):
            debug = True
        
    cam.init("video.mp4")
#    out.init()
#    if(debug):
#        deb.init()
    
    while(True):
#        try:
        frame = cam.get_image()
        list = net.getList(frame)
        result = an.getData(list)
#            out.out(result)
            
        if(debug):
            deb.printToTerm(result)
#            deb.updateImage(frame)
#           deb.updateNetText(list)
#           deb.updateResText(result)
                
#        finally:
#            out.close()

