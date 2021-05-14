import cv2
import numpy as np

#
#   이미지 전처리 과정
#입력받은 이미지를 전처리과정을 통해 이미지에서
#텍스트 영역 또는 글자 영역을 검출해내어 검출된 영역을
#32x32이미지의 크기로 리사이징하여 반환하는 기능을 한다.
#



def PreprocessingImage(targetImage):
    #
    # 보다 정확한 글자 영역의 추출을 위해서 입력 이미지 영상을
    # 그레이 이미지로 변환, 변환된 그레이 이미지를 가우시안 블러를 통해서
    # 이미지 영상의 잡음을 제거하고 경계선 검출(canny)을 통해 글자 부분의 윤곽을 검출한다.
    # 
    grayImage = cv2.cvtColor(targetImage, cv2.COLOR_BGR2GRAY)

    BlurredImage = cv2.GaussianBlur(grayImage,(5, 5),0)

    edgedImage = cv2.Canny(BlurredImage, 30, 150)

    #
    #경계선 검출이 끝난 이미지를 이진화하여 영상의 글자 부분을 강조
    #다음 이미지의 글자 영역을 번지게하여 덩어리를 만들 수 있도록 전처리라고 할 수 있을 것이다. 
    #(이 부분이 글자를 번지게 처리하는 과정에서 결과적으로 효과를 증대할 수 있지 않을까 추측함)
    #
    binarizedImage = cv2.adaptiveThreshold(edgedImage, 255, cv2.ADAPTIVE_THRESH_MEAN_C,  cv2.THRESH_BINARY_INV, 3, 30)

    #cv2.morphologyEx() 글자를 번지게하여 하나의 덩어리로써 검출될 수 있도록 하는 작업이다.
    morphedImage = cv2.morphologyEx(binarizedImage, cv2.MORPH_CLOSE, np.ones((6, 15), np.uint8))
    #위로 좀 더 번지게 만들어보기
    return morphedImage.copy()

def testPreprocessingImage(targetImage):
    #
    # 보다 정확한 글자 영역의 추출을 위해서 입력 이미지 영상을
    # 그레이 이미지로 변환, 변환된 그레이 이미지를 가우시안 블러를 통해서
    # 이미지 영상의 잡음을 제거하고 경계선 검출(canny)을 통해 글자 부분의 윤곽을 검출한다.
    # 
    grayImage = cv2.cvtColor(targetImage, cv2.COLOR_BGR2GRAY)

    BlurredImage = cv2.GaussianBlur(grayImage,(5, 5),0)

    edgedImage = cv2.Canny(BlurredImage, 30, 150)

    #
    #경계선 검출이 끝난 이미지를 이진화하여 영상의 글자 부분을 강조
    #다음 이미지의 글자 영역을 번지게하여 덩어리를 만들 수 있도록 전처리라고 할 수 있을 것이다. 
    #(이 부분이 글자를 번지게 처리하는 과정에서 결과적으로 효과를 증대할 수 있지 않을까 추측함)
    #
    #binarizedImage = cv2.adaptiveThreshold(edgedImage, 255, cv2.ADAPTIVE_THRESH_MEAN_C,  cv2.THRESH_BINARY_INV, 3, 30)

    #cv2.morphologyEx() 글자를 번지게하여 하나의 덩어리로써 검출될 수 있도록 하는 작업이다.
    #morphedImage = cv2.morphologyEx(binarizedImage, cv2.MORPH_CLOSE, np.ones((6, 15), np.uint8))
    return edgedImage.copy()
    
#
#   이미지의 저장된 경로와 파일명 변수이다.
#
fileName = 'test2.jpg'
filePath = 'C:\python\dev' + '/'
fullPath = filePath + fileName
  
#
#위에서 만들어진 절대경로를 통해서 numpy이미지를 오픈한다.
#numpy이미지를 opencv형태로 복호화하여 이미지 파일을 읽어온다.
#
inputImage = np.fromfile(fullPath, np.uint8)
image = cv2.imdecode(inputImage, cv2.IMREAD_COLOR)


resultImage = PreprocessingImage(image)

#
#위에서 전처리된 이미지 영상의 결과 이미지를 통해 각 글자 영역을 검출한다.
#검출된 글자 영역들을 반환한다.
#
contours, _ = cv2.findContours(resultImage.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#returnImage = cv2.resize(wordImage, dsize = (32,32), interpolation=cv2.INTER_AREA)
#filename = str(fileNameCount) + '.jpg'
#cv2.imwrite('C:\python\dev' + '/'+filename, returnImage)
#final = resize_to_pixel(20, squared)r > 0.45 and
mser = cv2.MSER_create()
for r in contours:
    #
    # 검출된 글자 영역들에서 각 영역들의 좌표를 반환받아
    # 입력 이미지 영상을 슬라이싱하여 반환한다.
    #
    (x, y, w, h) = cv2.boundingRect(r)
    if  w >= 5 and h >= 8:
        detectedWordImage = image[y:y+h, x:x+w]
        newResultImage = testPreprocessingImage(detectedWordImage)
        #grayImage = cv2.GaussianBlur(grayImage,(5, 5),0)
        #regions,_ = mser.detectRegions(newResultImage)
        rectImageContours, _ = cv2.findContours(newResultImage.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for r2 in rectImageContours:
            (x2, y2, w2, h2) = cv2.boundingRect(r2)   
            if  w >= 1 and h >= 1:   
                newDetectedWordImage = image[y+y2-5:y+y2+h2+5, x+x2-5:x+x2+w2+5]
                cv2.rectangle(image, (x+x2, y+y2), (x+x2 +w2, y+y2+h2), (0, 0, 255), 2)
                #cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
                #cv2.imshow("image", image)
                
cv2.imshow("dectectedimage", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

