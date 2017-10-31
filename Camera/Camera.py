'''
Created on Apr 10, 2017

@author: Lixingl
Get image and convert RGB to GrayScale 
'''
import cv2

camera = cv2.VideoCapture

def init(port):
    global camera
    camera = cv2.VideoCapture(port)
    
def get_image_old():
    global camera
    retval, im = camera.read()
    return im
    
def get_image():
    global camera
    retval, im = camera.read()
    return cv2.imencode('.jpg', im)
    
#convert to grayScale
def convert(im):
    if retval:
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        return gray_image

def test():
    cv2.namedWindow("cam-test", cv2.WINDOW_AUTOSIZE)
    for _ in range(10000):
        im = get_image_old()
        cv2.imshow("cam-test", im)
        cv2.waitKey(22)
    cv2.destroWindow("cam-test")

if __name__ == "__main__":
    init("video.mp4")
    test()



    
