import cv2
import numpy as np


def scaleArray(A, minVal, maxVal):
    tempData = A.copy().astype(np.float64)

    oldMinVal,oldMaxVal =  tempData.min(), tempData.max()
    
    scaleVal = float(maxVal-minVal) / float(oldMaxVal - oldMinVal)
    
    tempData -= oldMinVal
    tempData *= scaleVal
    tempData += minVal
    return tempData

def drawMap(m):
    m = scaleArray(m,0,255)
    m = m.astype(np.uint8)
    cv2.imwrite("map.png",m)



def checkValid(m):
    


a = np.random.randint(0,10,size=(10,10))


drawMap(a)