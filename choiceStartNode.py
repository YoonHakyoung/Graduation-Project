import json
import numpy as np

with open("/Users/yoon/python/node(linked).json", 'r') as nodefile:
    nodeData = json.load(nodefile)

inputWkt = [ 37.558996, 127.005254 ]

latiData = []

for i in range(10):
    fRange = i/1000
    for nodeID in nodeData:
        latiData.append(nodeData[nodeID][0])
           
    for lati in latiData:
        if lati in np.arange(inputWkt[0]-fRange, inputWkt[0]-fRange,fRange):
            print(lati)
