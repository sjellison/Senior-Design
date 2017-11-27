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
    while(not(camera.isOpened())):
        pass
    
def get_image_old():
    global camera
    retval, im = camera.read()
    if(not(retval)):
        print("Bad read")
    mi = im
    cv2.imencode('.jpg', mi)
    if(not(cv2.imwrite("img.jpg", mi))):
        print("Error writing image")
    cv2.waitKey(22)
    return im
    
def get_image(dest):
    global camera
    retval, im = camera.read()
    if(retval):
        suc, buf = cv2.imencode('.jpg', im)
        if(suc):
            if(not(cv2.imwrite(dest, im))):
                print("Failed to write image")
        else:
            print("Failed to encode image")
    else:
        print("Failed to read image")
    
    cv2.waitKey(22)
    return buf
    
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
    cv2.destroWindow("cam-test")

if __name__ == "__main__":
    init("video.mp4")
    test()



    
