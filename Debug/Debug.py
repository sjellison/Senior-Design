'''
Created on Oct 8, 2017

@author: bebop
'''
from tkinter import *
import threading
import time
from PIL import Image, ImageTk

root = Tk()
root.title("Debug Window")

mainFrame = Frame(root)
mainFrame.pack()

imageFrame = Frame(mainFrame)
imageLabel = Label(imageFrame)
imageLabel.pack()
imageFrame.pack(side="left", fill="both", expand="yes", pady=10)

dataFrame = Frame(mainFrame)
netTextBox = Text(dataFrame)
netTextBox.pack(side="top")
resTextBox = Text(dataFrame)
resTextBox.pack(side="bottom")
dataFrame.pack(side="right", fill="both", expand="yes", pady=10)

def init():
    global root
    root.mainloop()

def strtoimg(string):
    img = Image.open(string)
    photo = ImageTk.PhotoImage(img)
    return photo

def updateImage(img):
    global imageLabel, root
    
    imageLabel.configure(image=img)
    imageLabel.image = img

def updateNetText(data):
    global netTextBox
    netTextBox.insert(INSERT, data)
    netTextBox.pack
    
def updateResText(result):
    global resTextBox
    resTextBox.insert(INSERT, result)
    resTextBox.pack
    
#def updateData():
 #   global root
  #  root.event_generate(sequence)

if(__name__ == '__main__'):
    '''
    for i in range(1000):
        newText1 = "New Net Stuff" + str(i)
        newText2 = "New Res Stuff" + str(i)
        updateNetText(newText1)
        updateResText(newText2)
        if((i % 3) == 0):
            updateImage(strtoimg("C:/Users/bebop/Pictures/Saved Pictures/contemplation.jpg"))
        elif((i % 3) == 1):
            updateImage(strtoimg("C:/Users/bebop/Pictures/Saved Pictures/banner-958963__480.jpg"))
        else:
            updateImage(strtoimg("C:/Users/bebop/Pictures/Saved Pictures/project-management-2061635__480.jpg"))
        time.sleep(3)
    '''
    
    newText1 = "New Net Stuff"
    newText2 = "New Res Stuff"
    updateNetText(newText1)
    updateResText(newText2)
    updateImage(strtoimg("C:/Users/bebop/Pictures/Saved Pictures/contemplation.jpg"))
    root.mainloop()
    