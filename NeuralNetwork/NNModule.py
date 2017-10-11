# Pseudo code
#
# NN module
#
# Camera module will instantiate a NN module.
# Camera then will pass an image to the instantiated class.
# Ie:
# NN = new NNModule()
#
# while(true):
#     img = getImage()
#     NN.anaylyze(img)
#     wait 1 second


# class outline
# class NNModule:
#     def __init__(self):
#       Initialize the NN, set up any variables
#
#
#     def analyze(img):
#       Input:  img=opencv2.imread() formatted image
#       Output:
#       This runs the analysis code from example
#       This method will determine what object(s) are present in an image.
#       Once anaylsis is complete, output data
#
#
#     def drawbox_on_found_object(img, object_data):
#       This class will export the data
#
#     def img_out(img, highlighting):
#       Outputs the image, will draw a box around the found target if highlighting is true
#
#     def output(data):
#       This method will output statistical data as needed to the next stage


class NNModule:
    def __init__(self):
        # Initialize the NN, set up any variables
        print "Constructor here"

    def analyze(self, img):
        print "Take in image, classify with NN"

    def drawbox_on_found_objects(self, img, object_data):
        print "Draw a box on img!"

    def img_out(self, imt, highlighting):
        if highlighting:
            print "Highlighting disabled"
        else:
            print "Highlighting enabled"

    def output(self,data):
        print "This is where output data will occur"