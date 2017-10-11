'''
Created on Oct 8, 2017

@author: bebop
'''
from tkinter import *
import threading
import time
from PIL import Image, ImageTk

imageWidth = 200
imageHeight = 175

root = Tk()
root.title("Debug Window")

mainFrame = Frame(root, width=250, height=200)
mainFrame.pack()

imageFrame = Frame(mainFrame)
imageLabel = Label(imageFrame)
imageLabel.pack()
imageFrame.pack(side="left", fill="both", expand="yes", pady=10)

dataFrame = Frame(mainFrame)
netTextBox = Text(dataFrame, width=100, height=10)
netTextBox.pack(side="top")
resTextBox = Text(dataFrame, width=100, height=10)
resTextBox.pack(side="bottom")
dataFrame.pack(side="right", fill="both", expand="yes", pady=10)

'''
def init(w, h):
    global root, imageWidth, imageHeight
    imageWidth = w
    imageHeight = h
    root.mainloop()
'''

def strtoimg(string):
    img = Image.open(string)
    img = img.resize((200, 175), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(img)
    return photo

def updateImage(img):
    global imageLabel, root
    
    imageLabel.configure(image=img)
    imageLabel.image = img
    root.update()

def insertNetText(text):
    global netTextBox
    netTextBox.insert(INSERT, text) #adds new text to what's there
    netTextBox.pack
    root.update()

def updateNetText(data):
    global netTextBox
    netTextBox.delete("1.0", END)
    netTextBox.insert(INSERT, data) #adds new text to what's there
    netTextBox.pack
    root.update()
    
def updateResText(result):
    global resTextBox
    resTextBox.insert(INSERT, result)
    resTextBox.pack
    root.update()
    
def updateWindow():
    root.update()
    
#def updateData():
 #   global root
  #  root.event_generate(sequence)

if(__name__ == '__main__'):
    for i in range(15):
        newText1 = "New Net Stuff" + str(i)
        newText2 = "New Res Stuff" + str(i)
        updateNetText(newText1)
        updateResText(newText2)
        if(i % 3 == 0):
            updateImage(strtoimg("C:/Users/bebop/Pictures/Saved Pictures/contemplation.jpg"))
        elif(i % 3 == 1):
            updateImage(strtoimg("C:/Users/bebop/Pictures/Saved Pictures/project-management-2061635__480.jpg"))
        else:
            updateImage(strtoimg("C:/Users/bebop/Pictures/Saved Pictures/banner-958963__480.jpg"))
        time.sleep(1)
    