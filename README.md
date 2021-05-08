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
- Keras Tuner (`keras-tuner`)

## Usage
- `python datagen.py` : Generate `tfrecord` dataset from fonts.
- `python fit.py <folder_name> (or fit.sh)` : Train model.
- `python tune_hyper.py` : Find hyperparameters for best accuracy.
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

### Used Fonts
| Font File            | Font Name (English) | Font Name (Korean) | Author                        | License         | From       |
|----------------------|---------------------|--------------------|-------------------------------|-----------------|------------|
| KCCChassam.ttf       | KCCChassam          | KCC차쌤체          | 한국저작권위원회              | OFL             | 공유마당** |
| KCCImkwontack.ttf    | KCCImkwontack       | KCC임권택체        | 한국저작권위원회              | OFL             | 공유마당** |
| KoPubWorldDotum.ttf  | Kopub World Dotum   | Kopub World 돋움체 | 문화체육관광부, 한국출판회의  | 공공누리 1유형* | 공유마당** |
| GyenggiTitle.ttf     | Gyenggi Title       | 경기천년제목체     | 경기도                        | 공공누리 1유형* | 공유마당** |
| SeoulNamsan.ttf      | Seoul Namsan        | 서울남산체         | 서울시                        | 공공누리 1유형* | 공유마당** |
| SeoulHangang.ttf     | Seoul Hangang       | 서울한강체         | 서울시                        | 공공누리 1유형* | 공유마당** |
| JejuGothic.ttf       | Jeju Gothic         | 제주고딕체         | 제주시                        | 공공누리 1유형* | 공유마당** |
| JejuMyeongjo.ttf     | Jeju Myeongjo       | 제주명조체         | 제주시                        | 공공누리 1유형* | 공유마당** |
| PureunJeonnam.ttf    | Pureun Jeonnam      | 푸른전남체         | 전라남도                      | 공공누리 1유형* | 공유마당** |
| NanumGothic.ttf      | Nanum Gothic        | 나눔고딕           | (주)네이버, 재 네이버문화재단 | OFL             | 공유마당** |
| NanumBarunGothic.ttf | Nanum Barun Gothic  | 나눔바른고딕       | (주)네이버, 재 네이버문화재단 | OFL             | 공유마당** |
| NanumBarunpen.ttf    | Nanum Barun Pen     | 나눔바른펜         | (주)네이버, 재 네이버문화재단 | OFL             | 공유마당** |
| NanumPenScript.ttf   | Nanum Pen Script    | 나눔손글씨 붓체    | (주)네이버, 재 네이버문화재단 | OFL             | 공유마당** |
| NanumBrushScript.ttf | Nanum Brush Script  | 나눔손글씨 펜체    | (주)네이버, 재 네이버문화재단 | OFL             | 공유마당** |
| KCCDodamdodam.ttf    | KCC Dodamdodam      | KCC 도담도담체     | 한국저작권위원회              | OFL             | 공유마당** |

### Reference
\* 공공누리 1유형: [여기](https://www.kogl.or.kr/info/license.do#01-tab)를 참고하세요.  
\*\* 공유마당 : https://gongu.copyright.or.kr/gongu/bbs/B0000018/list.do?menuNo=200195

### Reference (English)
\* 공공누리 1유형(KOGL - Korean Open Goverment License, "Gonggongnuri" Type 1): Please refer [here](https://www.kogl.or.kr/info/license.do#05-tab) to get more information.  
\*\* 공유마당 : https://gongu.copyright.or.kr/gongu/bbs/B0000018/list.do?menuNo=200195