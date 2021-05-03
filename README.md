# OCR_KorEng
군산대학교 머신러닝종합설계 과목 프로젝트 - 국영문 혼합 텍스트 OCR

## Requisites
- Python 3.8
- Tensorflow (`tensorflow` or `tensorflow-gpu`)
- NumPy (`numpy`)
- SciPy (`scipy`)
- Pillow (`pillow`)
- OpenCV (`opencv-python`)
- FreeType (`freetype-py`)

## Usage
- `python datagen.py` : Generate `tfrecord` dataset from fonts.
- `python fit.py` : Train model.
- `python convert_lite.py` : Convert Tensorflow model to Tensorflow-lite model.
- `python predict.py` : Predict with generated model. 

## License
이 프로젝트는 MIT License를 따르고 있습니다. 이 프로젝트에서 사용하는 다른 오픈소스 라이브러리의 라이선스는 아래를 참고하십시오.  
This project (OCR_KorEng) is licensed under the MIT License. Also, various open source libraries are used in this project. Please refer below.

### Used Libraries
- [Tensorflow](https://www.tensorflow.org) is licensed under the Apache License 2.0.
- [NumPy](https://numpy.org) is licensed under the NumPy License. Refer [here](https://numpy.org/doc/stable/license.html).
- [SciPy](https://www.scipy.org) is licensed under the BSD-Clause-3 License.
- [Pillow](https://python-pillow.org/) is licensed under the HPND License. Refer [here](https://github.com/python-pillow/Pillow/blob/master/LICENSE).
- [OpenCV](https://opencv.org/) is licensed under the Apache License 2.0. (4.5.0 and higher)
- [FreeType](https://www.freetype.org/) is licensed under the FreeType License. Refer [here](https://gitlab.freedesktop.org/freetype/freetype/-/blob/master/docs/FTL.TXT).
