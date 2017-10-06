'''
Created on Sep 11, 2017

@author: bebop
'''
#import sys
#sys.path.append(".")
from getFrame import get_image
from Analysis import getData
from Network import getList
from Output import outputData

if __name__ == '__main__':
    
    
    #One pass through the system
    img = get_image
    l = getList
    analysis = getData(l)
    out = outputData(analysis)
    
    print(out)
    
    pass