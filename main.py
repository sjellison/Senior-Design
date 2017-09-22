'''
Created on Sep 11, 2017

@author: bebop
'''
from AutonomousProcessor.camera_controller.cameraContr.control.getFrame import get_image
from AutonomousProcessor.network.Network import getList
from AutonomousProcessor.analysis.Analysis import getData
from AutonomousProcessor.output.Output import outputData

if __name__ == '__main__':
    
    
    #One pass through the system
    img = get_image
    l = getList
    analysis = getData(l)
    out = outputData(analysis)
    
    pass