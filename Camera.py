'''
Created on Sep 6, 2017

@author: Sean Jellison
'''

import cv2

camera = cv2.VideoCapture(0) #subject to change if multiple cameras are attached

def getFrame():
    frame = camera.read()
    return frame

def releaseCam():
    del(camera)