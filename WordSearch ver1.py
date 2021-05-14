import cv2
import os
import numpy as np

fileName = 'numbers2.jpg'
filePath = 'C:\python\dev' + '/'
fullPath = filePath + fileName
inputImage = np.fromfile(fullPath, np.uint8)
image = cv2.imdecode(inputImage, cv2.IMREAD_COLOR)
grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#grayImage = cv2.GaussianBlur(grayImage,(5, 5),0)



mser = cv2.MSER_create()
regions,_ = mser.detectRegions(grayImage)

duplicateImage = image.copy()

#fileNameCount = 0
for j in regions:
    #fileNameCount = fileNameCount + 1
    (x, y, w, h) = cv2.boundingRect(np.reshape(j, (-1, 1, 2)))
    margin = 10
    cv2.rectangle(duplicateImage, (x-margin, y-margin), (x + w + margin, y + h + margin), (0, 255, 0), 1)
    #wordImage = duplicateImage[y-10 : (y+h+10), (x-10) : (x+w+10)]
    #returnImage = cv2.resize(wordImage, dsize = (32,32), interpolation=cv2.INTER_AREA)
    #filename = str(fileNameCount) + '.jpg'
    #cv2.imwrite('C:\python\dev' + '/'+filename, returnImage)   
    #cv2.waitKey(0)
cv2.imshow('mser', duplicateImage)
cv2.waitKey(0)
