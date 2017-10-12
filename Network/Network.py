
'''
This is a temporary module for testing and debugging while we wait for the actual network
'''

import random

def getList(frame):
    
    ret = []
    
    for i in range(10):
        name = "Ob" + str(i)
        xpos = random.randint(0, 255)
        ypos = random.randint(0, 255)
        width = random.randint(1, 200)
        height = random.randint(1, 200)
        
        ret[(i*5)] = name
        ret[(i*5) + 1] = xpos
        ret[(i*5) + 2] = ypos
        ret[(i*5) + 3] = width
        ret[(i*5) + 4] = height
        
    return ret
