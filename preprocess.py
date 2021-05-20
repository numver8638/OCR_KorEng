#
# preprocess.py
# - Preprocess image before recognition.
#
import cv2
import numpy as np


def preprocess_image(input_image):
    '''
    이미지 전처리 과정
    입력받은 이미지를 전처리과정을 통해 이미지에서
    텍스트 영역 또는 글자 영역을 검출해내어 검출된 영역을
    32x32이미지의 크기로 리사이징하여 반환하는 기능을 한다.
    
    Args:
        input_image (np.ndarray): 넘파이 배열로 변환된 이미지.

    Returns:
        32x32 크기 글자 이미지의 목록과 추출된 글자의 영역. (list[tuple[np.ndarray,tuple])
    '''
    # 입력 영상 이진화
    # 영상 라벨링을 위해 이진화 과정을 거쳐야한다.
    _, binaryImage = cv2.threshold(input_image , 0, 255, cv2.THRESH_OTSU + cv2.THRESH_BINARY_INV)
    # 라벨링을 수행하여, 라벨링된 개체 수, 중심좌표, 인덱스 등을 반환한다.
    num, labels, stats, centroids = cv2.connectedComponentsWithStats(binaryImage)

    # 검출된 글자 영역 개수만큼 이미지 슬라이싱을 통해
    # 글자 이미지를 추출한 후, 반환 형식에 맞게 이미지를 리사이징하여
    # 추출된 글자 이미지들을 리스트로 반환한다.
    words = []
    for i in range(1, num):
        x, y, w, h, area = stats[i]
        word = input_image[y-2 : (y+h+2), (x-2) : (x+w+2)]
        word = cv2.resize(word, dsize=(32, 32), interpolation=cv2.INTER_AREA) / 255.0
        words.append((word, (x,y,w,h)))
        
    return words
