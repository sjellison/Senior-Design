'''
Created on Apr 10, 2017

@author: Lixingl
Get image and convert RGB to GrayScale 
'''
import cv2

#cameraPort = 0;
camera = cv2.VideoCapture("video.mp4");

def get_image():
    retval, im = camera.read()
    return im
    

#convert to grayScale
def convert(im):
    if retval:
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        return gray_image

def test():
    im = get_image()
    cv2.namedWindow("cam-test", cv2.WINDOW_AUTOSIZE)
    cv2.imshow("cam-test", im)
    cv2.waitKey(1000)
    cv2.destroWindow("cam-test")

if __name__ == "__main__":
    test()



    
