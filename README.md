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
- [Keras Tuner](https://keras-team.github.io/keras-tuner/) is licensed under the Apache-2.0 License.

### Used Fonts
| Font File                      | Font Name (English)        | Font Name (Korean)       | Author                        | License         | From       |
|--------------------------------|----------------------------|--------------------------|-------------------------------|-----------------|------------|
| Cafe24 Ssurround air.ttf       | Cafe24 Ssurround air       | 카페24 써라운드 에어     | 카페24                        | OFL             | 눈누***    |
| DOS Gothic.ttf                 | DOS Gothic                 | 도스 고딕                | leedheo                       | MIT             | 눈누***    |
| DOS Myungjo.ttf                | DOS Myungjo                | 도스 명조                | leedheo                       | MIT             | 눈누***    |
| DOS Saemmul.ttf                | DOS Saemmul                | 도스 샘물                | leedheo                       | MIT             | 눈누***    |
| DungGeunMo.ttf                 | DungGeunMo                 | 둥근모                   | 길형진 (orioncactus)          | Public Domain   | 눈누***    |
| Gmarket Sans TTF Medium.ttf    | Gmarket Sans TTF Medium    | G마켓 산스 TTF Medium    | G마켓                         | OFL             | 눈누***    |
| GyeonggiBatang Regular.ttf     | GyeonggiBatang Regular     | 경기천년바탕 Regular     | 경기도                        | 공공누리 1유형* | 공유마당** |
| GyeonggiTitle.ttf              | GyeonggiTitle Light        | 경기천년제목 Light       | 경기도                        | 공공누리 1유형* | 공유마당** |
| HangultuelGothic-Regular.ttf   | HangultuelGothic-Regular   | 한글틀고딕Regular        | 한글마을                      | OFL             | 눈누***    |
| Iropke Batang Medium.ttf       | Iropke Batang Medium       | 이롭게 바탕체 Medium     | 이롭게                        | OFL             | 눈누***    |
| JejuGothic.ttf                 | JejuGothic                 | 제주고딕                 | 제주시                        | 공공누리 1유형* | 공유마당** |
| JejuHallasan.ttf               | JejuHallasan               | 제주한라산               | 제주시                        | 공공누리 1유형* | 공유마당** |
| JejuMyeongjo.ttf               | JejuMyeongjo               | 제주명조                 | 제주시                        | 공공누리 1유형* | 공유마당** |
| KCCChassam.ttf                 | KCCChassam                 | KCC차쌤체                | 한국저작권위원회              | OFL             | 공유마당** |
| KCCDodamdodam.ttf              | KCCDodamdodam              | KCC도담도담체            | 한국저작권위원회              | OFL             | 공유마당** |
| KCCImkwontaek.ttf              | KCCImkwontaek              | KCC임권택체              | 한국저작권위원회              | OFL             | 공유마당** |
| KHNPHanuoolim.ttf              | KHNPHanuoolim              | 한수원 한울림            | 한국수력원자력                | 공공누리 1유형* | 공유마당** |
| KoPubWorldDotum.ttf            | KoPubWorldDotum Light      | KoPubWorld돋움체 Light   | 문화체육관광부, 한국출판회의  | 공공누리 1유형* | 공유마당** |
| Nanum BaReunHiPi.ttf           | Nanum BaReunHiPi           | 나눔손글씨 바른히피      | (주)네이버, 재 네이버문화재단 | OFL             | 눈누***    |
| Nanum Brush Script.ttf         | Nanum Brush Script         | 나눔손글씨 붓            | (주)네이버, 재 네이버문화재단 | OFL             | 공유마당** |
| Nanum JangMiCe.ttf             | Nanum JangMiCe             | 나눔손글씨 장미체        | (주)네이버, 재 네이버문화재단 | OFL             | 눈누***    |
| Nanum JungHagSaeng.ttf         | Nanum JungHagSaeng         | 나눔손글씨 중학생        | (주)네이버, 재 네이버문화재단 | OFL             | 눈누***    |
| Nanum NeuRisNeuRisCe.ttf       | Nanum NeuRisNeuRisCe       | 나눔손글씨 느릿느릿체    | (주)네이버, 재 네이버문화재단 | OFL             | 눈누***    |
| Nanum OeHarMeoNiGeurSsi.ttf    | Nanum OeHarMeoNiGeurSsi    | 나눔손글씨 외할머니글씨  | (주)네이버, 재 네이버문화재단 | OFL             | 눈누***    |
| Nanum Pen Script.ttf           | Nanum Pen Script           | 나눔손글씨 펜            | (주)네이버, 재 네이버문화재단 | OFL             | 공유마당** |
| Nanum YeonJiCe.ttf             | Nanum YeonJiCe             | 나눔손글씨 연지체        | (주)네이버, 재 네이버문화재단 | OFL             | 눈누***    |
| NanumBarunGothic.ttf           | NanumBarunGothic           | 나눔바른고딕             | (주)네이버, 재 네이버문화재단 | OFL             | 공유마당** |
| NanumBarunpen.ttf              | NanumBarunpen              | 나눔바른펜               | (주)네이버, 재 네이버문화재단 | OFL             | 공유마당** |
| NanumGothic.ttf                | NanumGothic                | 나눔고딕                 | (주)네이버, 재 네이버문화재단 | OFL             | 공유마당** |
| NanumMyeongjo.ttf              | NanumMyeongjo              | 나눔명조                 | (주)네이버, 재 네이버문화재단 | OFL             | 눈누***    |
| NeoDunggeunmo.ttf              | NeoDunggeunmo              | Neo둥근모                | Dalgona                       | OFL             | 눈누***    |
| PureunJeonnam.ttf              | PureunJeonnam              | 푸른전남                 | 전라남도                      | 공공누리 1유형* | 공유마당** |
| Samgukji Korean Font.ttf       | Samgukji Korean Font       | 삼국지3글꼴              | leedheo                       | MIT             | 눈누***    |
| SeoulHangang.ttf               | SeoulHangang B             | 서울한강체 B             | 서울시                        | 공공누리 1유형* | 공유마당** |
| SeoulNamsan.ttf                | SeoulNamsan B              | 서울남산체 B             | 서울시                        | 공공누리 1유형* | 공유마당** |
| Spoqa Han Sans Neo Regular.ttf | Spoqa Han Sans Neo Regular | 스포카 한 산스 R         | 스포카                        | OFL             | 눈누***    |
| TmonMonsori Black.ttf          | TmonMonsori Black          | Tmon몬소리 Black         | 티몬                          | OFL             | 눈누***    |

### Reference
\* 공공누리 1유형: [여기](https://www.kogl.or.kr/info/license.do#01-tab)를 참고하세요.  
\*\* 공유마당 : https://gongu.copyright.or.kr/gongu/bbs/B0000018/list.do?menuNo=200195
\*\*\* 눈누: https://noonnu.cc/

### Reference (English)
\* 공공누리 1유형(KOGL - Korean Open Goverment License, "Gonggongnuri" Type 1): Please refer [here](https://www.kogl.or.kr/info/license.do#05-tab) to get more information.  
\*\* 공유마당 : https://gongu.copyright.or.kr/gongu/bbs/B0000018/list.do?menuNo=200195
\*\*\* 눈누: https://noonnu.cc/