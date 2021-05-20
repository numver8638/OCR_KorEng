import cv2
import numpy as np

#
#    이미지 전처리 과정
#    입력받은 이미지를 전처리과정을 통해 이미지에서
#    텍스트 영역 또는 글자 영역을 검출해내어 검출된 영역을
#    32x32이미지의 크기로 리사이징하여 반환하는 기능을 한다.
#

def preprocess_image(targetImage)
    # 입력 영상 이진화
    # 영상 라벨링을 위해 이진화 과정을 거쳐야한다.
    _, binaryImage = cv2.threshold(targetImage , 0, 255, cv2.THRESH_OTSU + cv2.THRESH_BINARY_INV)
    # 라벨링을 수행하여, 라벨링된 개체 수, 중심좌표, 인덱스 등을 반환한다.
    num, labels, stats, centroids = cv2.connectedComponentsWithStats(binaryImage)

    # 검출된 글자 영역 개수만큼 이미지 슬라이싱을 통해
    # 글자 이미지를 추출한 후, 반환 형식에 맞게 이미지를 리사이징하여
    # 추출된 글자 이미지들을 리스트로 반환한다.
    words = []
    for i in range(1, num):
        x, y, w, h, area = stats[i]
        word = targetImage[y-2 : (y+h+2), (x-2) : (x+w+2)]
        word = cv2.resize(word, dsize = (32, 32), interpolation=cv2.INTER_AREA)
        words.append(word)
        
    return words