try:
    from tkinter import * #this is for Python3
except:
    from Tkinter import *

import time
from PIL import Image, ImageTk, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

imageWidth = 200
imageHeight = 175

root = None
mainFrame = None
imageFrame = None
imageLabel = None
dataFrame = None
netTextBox = None
resTextBox = None

'''
Initializes the window to use
'''
def init():
    global root, mainFrame, imageFrame, imageLabel, dataFrame, netTextBox, resTextBox
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
    resTextBox = Text(mainFrame, width=100, height=10)
    resTextBox.pack(side="bottom")
    dataFrame.pack(side="right", fill="both", expand="yes", pady=10)
    updateWindow()

'''
Converts a path to an image
return: a PhotoImage
'''
def strtoimg(string):
    img = Image.open(string)
    img = img.resize((200, 175), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(img)
    return photo

'''
Replaces the image in the image frame with the given image
'''
def updateImage(img):
    global imageLabel, root
    imageLabel.configure(image=img)
    imageLabel.image = img

'''
Appends the given text to the end of the network text field
'''
def insertNetText(text):
    global netTextBox
    netTextBox.insert(INSERT, text) #adds new text to what's there
    netTextBox.pack
    #root.update()

'''
Replaces the text in the network text field with the given text
'''
def updateNetText(data):
    global netTextBox
    netTextBox.delete("1.0", END)
    netTextBox.insert(INSERT, data) #adds new text to what's there
    netTextBox.pack
    #root.update()
    
'''
Appends the given text to the end of the results text field
'''
def insertResText(text):
    global resTextBox
    resTextBox.insert(INSERT, text)
    resTextBox.pack
    #root.update()
    
'''
Replaces the text in the results text field with the given text
'''
def updateResText(result):
    global resTextBox
    resTextBox.delete("1.0", END)
    resTextBox.insert(INSERT, result)
    resTextBox.pack
    #root.update()
    
def printToTerm(data=[]):
    for _ in data:
        print(_)
    
'''
Updates the window. Shouldn't need to be called, but it's there if the need arises.
'''
def updateWindow():
    root.update()

'''
Runs if this file is run as a main file. Used for debugging.
'''
if(__name__ == '__main__'):
    init()

    for i in range(100):
        newText1 = "New Net Stuff" + str(i)
        newText2 = "New Res Stuff" + str(i)
        updateNetText(newText1)
        updateResText(newText2)

        if(i % 3 == 0):
            updateImage(strtoimg("C:/Users/bebop/Pictures/Saved Pictures/oogieboogie.jpg"))
        elif(i % 3 == 1):
            updateImage(strtoimg("C:/Users/bebop/Pictures/Saved Pictures/contemplation.jpg"))
        else:
            updateImage(strtoimg("C:/Users/bebop/Pictures/Saved Pictures/banner-958963__480.jpg"))
        updateWindow()

        time.sleep(1)
    root.destroy()
