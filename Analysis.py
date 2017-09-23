'''
Created on Aug 30, 2017

@author: Sean Jellison
'''

'''
THINGS TO PUT IN THE CONFIG FILE
  Camera Focal Length
  A list of desired data (distance, orientation, isobject and target for isobject, etc.)
  Database information
  

THINGS TO GET FROM THE DATABASE
  Object width based on the name of the object
'''


#from ..network.Network import getList
import MySQLdb

#database = MySQLdb.connect("localhost", "user", "password", "DatabaseName")
database = MySQLdb.connect("localhost", "analysis", "dec1710", "Objects")
dbcursor = database.cursor()

'''
Returns a list of data for every object in the list. Assumes a strict data formating.
list - the list of objects. data must be in the form: name, xpos, ypos, width, height
return - an array of data for every object. data is in the form: object name1, data type1, related data, data type2..., object name2...
'''
def getData(list):
    data = {}
    datacounter = 0
    for i in range((len(list)/5)):
        obName = list[i]
        x = list[i + 1]
        y = list[i + 2]
        width = list[i + 3]
        height = list[i + 4]
        
        #object name, data type, related data, data type..., related data..., object name...
        data[datacounter] = obName
        datacounter = datacounter + 1
        
        data[datacounter] = 'xposition'
        datacounter = datacounter + 1
        
        data[datacounter] = (x + width)/2
        datacounter = datacounter + 1
        
        data[datacounter] = 'yposition'
        datacounter = datacounter + 1
        
        data[datacounter] = (y + height)/2
        datacounter = datacounter + 1
        
        data[datacounter] = 'distance'
        datacounter = datacounter + 1
        
        data[datacounter] = getDistance(obName, width)
        
    return data
    

'''
Determines the distance to the object
  name - name of the object for querying
  width - number of pixels wide the object is
  
  return - the distance to the object. units of measurement are dependent on the focal length and objectwidth units
''' 
def getDistance(name, width):
    #TODO
    #Need to test the database query
    
    query = "SELECT width FROM objects WHERE name == '%s'" % (name)
             
    try:
        dbcursor.execute(query)
        objectwidth = dbcursor[width]
        #objectwidth = 3.75 #meters
        focallength = .0036 #meters
        dbcursor.close()
        return ((focallength * objectwidth) / width)

    except:
        print("Error: Could not fetch data")

'''
Calculates the focal length for the camera given the object's actual width, number of pixels wide the object is in the image,
and distance to the object. The objectwidth and distance must be in the same units for accurate results. Focal length will
then be in those same units as well.
'''
def getFocalLength(objectwidth, width, distance):
    return (distance / objectwidth) * width

'''
Gets the orientation of the object relative to the camera and the object's "front"
'''    
def getOrientation():
    #TODO
    return