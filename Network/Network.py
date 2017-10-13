
'''
This is a temporary module for testing and debugging while we wait for the actual network
'''

import random

def getList(frame):
    
    ret = []
    
    for i in range(10):
#        print("Network: " + str(i))
        name = "airport"
#        print("Network: " + name)
        xpos = random.randint(0, 255)
#        print("Network: " + str(xpos))
        ypos = random.randint(0, 255)
#        print("Network: " + str(ypos))
        width = random.randint(1, 200)
#        print("Network: " + str(width))
        height = random.randint(1, 200)
#        print("Network: " + str(height))
        
        #ret[(i*5)] = name
        #ret[(i*5) + 1] = xpos
        #ret[(i*5) + 2] = ypos
        #ret[(i*5) + 3] = width
        #ret[(i*5) + 4] = height
        
        ret.append(name)
        ret.append(xpos)
        ret.append(ypos)
        ret.append(width)
        ret.append(height)
        
    return ret
