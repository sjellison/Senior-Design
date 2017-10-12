'''
Created on Apr 10, 2017

@author: Lixingl
Get image and convert RGB to GrayScale 
'''
import cv2
import NNModule

cameraPort = 0;
camera = cv2.VideoCapture(cameraPort);
NN = new NNModule

#capture a image
def get_image():
    global im 
    retval, im = camera.read()
    return im

#convert to grayScale
def convert():
    image = cv2.imread(im)
    NN.analyze(image)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('gray_image.png', gray_image)
    cv2.imshow('gray_image', gray_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

del(camera)


    
