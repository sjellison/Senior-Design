'''
Created on Aug 30, 2017

@author: Sean Jellison
'''

import MySQLdb

database = MySQLdb.connect("localhost", "analysis", "Dec_1710", "Objects")
dbcursor = database.cursor()

debug = False

'''
Sets the debug flag to true and prints out some debug results
'''
def debug():
    debug = True
    print("Testing database connection...")
    print(dbcursor.execute("SELECT VERSION()"))
    print("Database version: %s" % dbcursor.fetchone())
    print("Database test complete")

def closeDb():
    dbcursor.close()

'''
Returns a list of data for every object in the list. Assumes a strict data formating.
list - the list of objects. data must be in the form: name, xpos, ypos, width, height
return - an array of data for every object. data is in the form: object name1, data type1, related data, data type2..., object name2...
'''
def getData_old(dataList=[]):
    #data = {}
    data = []
    #datacounter = 0
    count = 0
    for i in dataList:
        if(count == 0):
            obName = i
        elif(count == 1):
            x = i
        elif(count == 2):
            y = i
        elif(count == 3):
            width = i
        elif(count == 4):
            height = i
            
            #object name, data type, related data, data type..., related data..., object name...
            #data[datacounter] = obName
            data.append(obName)
            #datacounter = datacounter + 1
            
            #data[datacounter] = 'xposition'
            data.append('xposition')
            #datacounter = datacounter + 1
            
            #data[datacounter] = (x + width)/2
            data.append(x + (width/2))
            #datacounter = datacounter + 1
            
            #data[datacounter] = 'yposition'
            data.append('yposition')
            #datacounter = datacounter + 1
            
            #data[datacounter] = (y + height)/2
            data.append(y + (height/2))
            #datacounter = datacounter + 1
            
            #data[datacounter] = 'distance'
            data.append('distance')
            #datacounter = datacounter + 1
            
            #data[datacounter] = getDistance(obName, width)
            data.append(getDistance(obName, width))
            
        count = (count + 1) % 5
        
    return data
    
def getData(data={}):
    d = []
    for i in data:
        d.append(i["name"])
        d.append(i["score"])
        d.append(getDistance(i["name"], 10)) #currently an arbitrary width

    return d

'''
Determines the distance to the object
  name - name of the object for querying
  width - number of pixels wide the object is
  
  return - the distance to the object. units of measurement are dependent on the focal length and objectwidth units
''' 
def getDistance(name, width):
    
    query = """SELECT width 
                FROM Objects
                WHERE name='%s'""" % (name)
    if(debug):
        print("Query used: " + query)

    try:
        if(debug):
            print("Executing query...")
        dbcursor.execute(query)
        objectwidth = dbcursor.fetchone()
        if(debug):
            print("Query result: " + str(objectwidth))
        #objectwidth = 3.75 #meters
        focallength = .0036 #meters
        return ((focallength * objectwidth) / width)

    except:
        print("Error: Could not fetch data for " + name)
   
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