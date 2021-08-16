#
# preprocess.py
# - Preprocess image before recognition.
#
import cv2
import numpy as np


def _merge_rect(left, right):
    if left[0] > right[0]:
        left, right = right, left

    x1, y1, w1, h1 = left
    x2, y2, w2, h2 = right

    if (x1 + w1) < x2 or (y1 + h1) < y2 or y1 > (y2 + h2):
        # rect not conflict
        return None
    else:
        x = min(x1, x2)
        y = min(y1, y2)
        w = max(x1 + w1, x2 + w2) - x
        h = max(y1 + h1, y2 + h2) - y

        return x, y, w, h 


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
    grey_image = cv2.cvtColor(input_image, cv2.COLOR_RGB2GRAY)

    # 입력 영상 이진화
    # 영상 라벨링을 위해 이진화 과정을 거쳐야한다.
    _, binaryImage = cv2.threshold(grey_image , 0, 255, cv2.THRESH_OTSU|cv2.THRESH_BINARY_INV)
    # 라벨링을 수행하여, 라벨링된 개체 수, 중심좌표, 인덱스 등을 반환한다.
    _, _, stats, _ = cv2.connectedComponentsWithStats(binaryImage)

    rects = [(x, y-5, w, h+10) for x, y, w, h, _ in stats[1:]]

    loop = True
    while loop:
        loop = False

        for i in range(len(rects)):
            if rects[i] is None:
                continue

            for j in range(len(rects)):
                if rects[i] == rects[j] or rects[j] is None:
                    continue

                merged = _merge_rect(rects[i], rects[j])
                if merged is not None:
                    loop = True
                    rects[i] = merged
                    rects[j] = None

        rects = list(filter(lambda e: e is not None, rects))

    # 검출된 글자 영역 개수만큼 이미지 슬라이싱을 통해
    # 글자 이미지를 추출한 후, 반환 형식에 맞게 이미지를 리사이징하여
    # 추출된 글자 이미지들을 리스트로 반환한다.
    words = []
    for x, y, w, h in rects:
        word = binaryImage[y : (y+h), (x) : (x+w)]

        if word.size == 0:
            continue

        height, width = word.shape

        if width < 5 or height < 5:
            continue

        if width > 28 or height > 28:
            scale = 28 / max(width, height)
            
            if scale < 0.1:
                print("scale (", scale, ") is too small. ignore it.")
                continue

            word = cv2.resize(word, (0, 0), fx=scale, fy=scale)

        height, width = word.shape

        if width > 32 or height > 32:
            print('rect in (', x, y, x+w, y+h, ') is overflowed. ignore it.')
            continue

        top = (32 - height) // 2
        bottom = 32 - (height + top)
        left = (32 - width) // 2
        right = 32 - (width + left)

        word = cv2.copyMakeBorder(word, top, bottom, left, right, cv2.BORDER_CONSTANT, value=0)
        word = word.astype(np.float32)
        word /= 255.0

        words.append((word, (x,y,w,h)))
        
    return words
