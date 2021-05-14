import cv2
import numpy as np

#
#   이미지 전처리 과정
#입력받은 이미지를 전처리과정을 통해 이미지에서
#텍스트 영역 또는 글자 영역을 검출해내어 검출된 영역을
#32x32이미지의 크기로 리사이징하여 반환하는 기능을 한다.
#


#
#   이미지의 저장된 경로와 파일명 변수이다.
#
fileName = 'test3.png'
filePath = 'C:\python\dev' + '/'
fullPath = filePath + fileName

#
#위에서 만들어진 절대경로를 통해서 numpy이미지를 오픈한다.
#numpy이미지를 opencv형태로 복호화하여 이미지 파일을 읽어온다.
#
inputImage = np.fromfile(fullPath, np.uint8)
image = cv2.imdecode(inputImage, cv2.IMREAD_COLOR)


#
# 보다 정확한 글자 영역의 추출을 위해서 입력 이미지 영상을
# 그레이 이미지로 변환, 변환된 그레이 이미지를 가우시안 블러를 통해서
# 이미지 영상의 잡음을 제거하고 경계선 검출(canny)을 통해 글자 부분의 윤곽을 검출한다.
# 

grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

BlurredImage = cv2.GaussianBlur(grayImage,(5, 5),0)

edgedImage = cv2.Canny(BlurredImage, 30, 150)

#
#경계선 검출이 끝난 이미지를 이진화하여 영상의 글자 부분을 강조
#다음 이미지의 글자 영역을 번지게하여 덩어리를 만들 수 있도록 전처리라고 할 수 있을 것이다. 
#(이 부분이 글자를 번지게 처리하는 과정에서 결과적으로 효과를 증대할 수 있지 않을까 추측함)
#
binarizedImage = cv2.adaptiveThreshold(edgedImage, 255, cv2.ADAPTIVE_THRESH_MEAN_C,  cv2.THRESH_BINARY_INV, 3, 30)

#cv2.morphologyEx() 글자를 번지게하여 하나의 덩어리로써 검출될 수 있도록 하는 작업이다.
#morphedImage = cv2.morphologyEx(binarizedImage, cv2.MORPH_CLOSE, np.ones((3,3), np.uint8))
morphedImage = cv2.erode(binarizedImage, np.ones((1,1), np.uint8), iterations = 1)
morphedImage = cv2.dilate(morphedImage, np.ones((2,2), np.uint8), iterations = 1)
cv2.imshow("imawge", morphedImage)
cv2.waitKey(0)

#
#위에서 전처리된 이미지 영상의 결과 이미지를 통해 각 글자 영역을 검출한다.
#검출된 글자 영역들을 반환한다.
#
contours, _ = cv2.findContours(morphedImage.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for r in contours:
    #
    # 검출된 글자 영역들에서 각 영역들의 좌표를 반환받아
    # 입력 이미지 영상을 슬라이싱하여 반환한다.
    #
    (x, y, w, h) = cv2.boundingRect(r)
    if  w >= 2 and h >= 4:
        rectSize = 0
        #returnImage = cv2.resize(wordImage, dsize = (32,32), interpolation=cv2.INTER_AREA)
        #filename = str(fileNameCount) + '.jpg'
        #cv2.imwrite('C:\python\dev' + '/'+filename, returnImage)
        #final = resize_to_pixel(20, squared)r > 0.45 and
        
        #
        #검출된 글자 영역에 대한 사각형 좌표를 인자로 설정.
        #인자로 설정한 사각형 좌표를 통해 이미지에 빨간 사각형을 그린다.
        #
        cv2.rectangle(image, (x-rectSize, y-rectSize), (x + w+rectSize, y + h+rectSize), (0, 0, 255), 2)
        #
        #실제로 이미지를 슬라이싱하여 추출하는 코드이다.
        #       
        detectedWordImage = image[y-rectSize:y+h+rectSize, x-rectSize:x+w+rectSize]
        cv2.imshow("image", image)
        cv2.imshow("dectectedimage", detectedWordImage)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
