#
# preprocess.py
# - Preprocess image before recognition.
#
import cv2
import numpy as np

class Preprocessor:
    '''
    Simple image preprocessor with customizable layers.
    Idea from: tf.keras.models.Sequential

    Args:
        layers (list): filters to be passed on image.
    '''
    
    def __init__(self, layers=[]) -> None:
        self._layers = layers

    def preprocess(self, input_image) -> np.ndarray:
        '''
        Preprocess image with predefined filters.

        Args:
            input_image (np.ndarray) : original image to preprocess.

        Returns:
            preprocessed image. (np.ndarray)
        '''
        filtered_image = input_image
        
        for filter in self._layers:
            filtered_image = filter(filtered_image)
        
        return filtered_image


def image_roi(input_image):
    '''
    이미지 전처리 과정
    입력받은 이미지를 전처리과정을 통해 이미지에서
    텍스트 영역 또는 글자 영역을 검출해내어 검출된 영역을
    32x32이미지의 크기로 리사이징하여 반환하는 기능을 한다.
    
    Args:
        input_image (np.ndarray): 넘파이 배열로 변환된 이미지.

    Returns:
        32x32 크기 글자 이미지의 목록. (list[np.ndarray])
    '''
    preprocessor = Preprocessor(layers=[
        # 보다 정확한 글자 영역의 추출을 위해서 입력 이미지 영상을
        # 그레이 이미지로 변환, 변환된 그레이 이미지를 가우시안 블러를 통해서
        # 이미지 영상의 잡음을 제거하고 경계선 검출(canny)을 통해 글자 부분의 윤곽을 검출한다.
        lambda image: cv2.cvtColor(image, cv2.COLOR_BGR2GRAY),
        lambda image: cv2.GaussianBlur(image, (5,5), 0),
        lambda image: cv2.Canny(image, 30, 150),
        # 경계선 검출이 끝난 이미지를 이진화하여 영상의 글자 부분을 강조
        # 다음 이미지의 글자 영역을 번지게하여 덩어리를 만들 수 있도록 전처리라고 할 수 있다.
        lambda image: cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 3, 30),
        lambda image: cv2.erode(image, np.ones((1, 1), np.uint8), iterations=1),
        lambda image: cv2.dilate(image, np.ones((2, 2), np.uint8), iterations=1)
    ])

    # 이미지 글자 영역을 검출하는데 조정되는 변수들이다.
    rectSize = 1
    
    image = input_image.copy()
    wordImages = []

    preprocessedImage = preprocessor.preprocess(image)

    # 위에서 전처리된 이미지 영상의 결과 이미지를 통해 각 글자 영역을 검출한다.
    contours1, _ = cv2.findContours(preprocessedImage, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for r1 in contours1:
        # 검출된 글자 영역들에서 각 영역들의 좌표를 반환받아
        # 입력 이미지 영상을 슬라이싱하여 반환한다.
        (x, y, w, h) = cv2.boundingRect(r1)
        if w >= 2 and h >= 4:
            detectedWordImage = image[y : y+h, x : x+w]

            # 최대한 많고, 정확하게 글자 영역을 검출하기 위해서
            # 검출된 글자 영역을 잘라내어 잘라낸 부분만 다시 한번 더 전처리 과정을 거친 후
            # 글자 영역을 재 검출하여 새로운 글자 영역을 검출한다.        
            newPreprocessedImage = preprocessor.preprocess(detectedWordImage)
            contours2, _ = cv2.findContours(newPreprocessedImage, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            for r2 in contours2:
                (x2, y2, w2, h2) = cv2.boundingRect(r2)
                if w2 >= 2 and h2 >= 2:
                    newDetectedWordImage = image[y+y2-rectSize : y+y2+h2+rectSize, x+x2-rectSize : x+x2+w2+rectSize]

                    # 검출된 글자 이미지를 32x32의 크기 이미지로 축소 변환하여
                    # 변환된 이미지들을 리스트로 만들어 리턴함.
                    wordImage = cv2.resize(newDetectedWordImage, dsize = (32, 32), interpolation=cv2.INTER_AREA)
                    wordImages.append(wordImage)
        
    return wordImages