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
- `python recog.py <image>` : Recognize text with generated model. 

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
| Font File                          | Font Name (English)            | Font Name (Korean)          | Author                        | License         | From            |
|------------------------------------|--------------------------------|-----------------------------|-------------------------------|-----------------|-----------------|
| Cafe24 Ssurround air.ttf           | Cafe24 Ssurround air           | 카페24 써라운드 에어        | 카페24                        | OFL             | 눈누***         |
| Chilgok_Cye.ttf                    | Chilgok_Cye                    | 칠곡할매 추유을체           | 칠곡군                        | 공공누리 1유형* | 공유마당**      |
| Chilgok_kyb.ttf                    | Chilgok_kyb                    | 칠곡할매 김영분체           | 칠곡군                        | 공공누리 1유형* | 공유마당**      |
| Chilgok_ljh.ttf                    | Chilgok_ljh                    | 칠곡할매 이종희체           | 칠곡군                        | 공공누리 1유형* | 공유마당**      |
| Chilgok_lws.ttf                    | Chilgok_lws                    | 칠곡할매 이원순체           | 칠곡군                        | 공공누리 1유형* | 공유마당**      |
| DOS Gothic.ttf                     | DOS Gothic                     | 도스 고딕                   | leedheo                       | MIT             | 눈누***         |
| DOS Myungjo.ttf                    | DOS Myungjo                    | 도스 명조                   | leedheo                       | MIT             | 눈누***         |
| DOS Saemmul.ttf                    | DOS Saemmul                    | 도스 샘물                   | leedheo                       | MIT             | 눈누***         |
| DungGeunMo.ttf                     | DungGeunMo                     | 둥근모                      | 길형진 (orioncactus)          | Public Domain   | 눈누***         |
| EnvironmentR.ttf                   | EnvironmentR                   | 환경R                       | 한국환경공단                  | 공공누리 1유형* | 공유마당**      |
| GimhaeGaya.ttf                     | GimhaeGaya                     | 김해가야체                  | 김해시                        | 공공누리 1유형* | 공유마당**      |
| Gmarket Sans TTF Medium.ttf        | Gmarket Sans TTF Medium        | G마켓 산스 TTF Medium       | G마켓                         | OFL             | 눈누***         |
| GyeonggiBatang Regular.ttf         | GyeonggiBatang Regular         | 경기천년바탕 Regular        | 경기도                        | 공공누리 1유형* | 공유마당**      |
| GyeonggiTitle Medium.ttf           | GyeonggiTitle Medium           | 경기천년제목 Medium         | 경기도                        | 공공누리 1유형* | 공유마당**      |
| HangultuelGothic-Regular.ttf       | HangultuelGothic-Regular       | 한글틀고딕Regular           | 한글마을                      | OFL             | 눈누***         |
| Iropke Batang Medium.ttf           | Iropke Batang Medium           | 이롭게 바탕체 Medium        | 이롭게                        | OFL             | 눈누***         |
| JejuGothic.ttf                     | JejuGothic                     | 제주고딕                    | 제주시                        | 공공누리 1유형* | 공유마당**      |
| JejuHallasan.ttf                   | JejuHallasan                   | 제주한라산                  | 제주시                        | 공공누리 1유형* | 공유마당**      |
| JejuMyeongjo.ttf                   | JejuMyeongjo                   | 제주명조                    | 제주시                        | 공공누리 1유형* | 공유마당**      |
| JS Dongkang.ttf                    | JS Dongkang                    | 정선동강                    | 정선군                        | 공공누리 1유형* | 공유마당**      |
| KCCChassam.ttf                     | KCCChassam                     | KCC차쌤체                   | 한국저작권위원회              | OFL             | 공유마당**      |
| KCCDodamdodam.ttf                  | KCCDodamdodam                  | KCC도담도담체               | 한국저작권위원회              | OFL             | 공유마당**      |
| KCCImkwontaek.ttf                  | KCCImkwontaek                  | KCC임권택체                 | 한국저작권위원회              | OFL             | 공유마당**      |
| KCCMurukmuruk.ttf                  | KCCMurukmuruk                  | KCC무럭무럭                 | 한국저작권위원회              | OFL             | 공유마당**      |
| KHNPHanuoolim.ttf                  | KHNPHanuoolim                  | 한수원 한울림               | 한국수력원자력                | 공공누리 1유형* | 공유마당**      |
| KoPubWorldBatang Medium.ttf        | KoPubWorldBatang Medium        | KoPubWorld바탕체 Medium     | 문화체육관광부, 한국출판회의  | 공공누리 1유형* | 공유마당**      |
| KoPubWorldDotum Medium.ttf         | KoPubWorldDotum Medium         | KoPubWorld돋움체 Medium     | 문화체육관광부, 한국출판회의  | 공공누리 1유형* | 공유마당**      |
| Nanum ABbaEuiYeonAePyeonJi.ttf     | Nanum ABbaEuiYeonAePyeonJi     | 나눔손글씨 아빠의 연애편지  | (주)네이버, 재 네이버문화재단 | OFL             | NAVER CLOVA**** |
| Nanum ABbaGeurSsi.ttf              | Nanum ABbaGeurSsi              | 나눔손글씨 아빠글씨         | (주)네이버, 재 네이버문화재단 | OFL             | NAVER CLOVA**** |
| Nanum AGiSaRangCe.ttf              | Nanum AGiSaRangCe              | 나눔손글씨 아기사랑체       | (주)네이버, 재 네이버문화재단 | OFL             | NAVER CLOVA**** |
| Nanum AInMamSonGeurSsi.ttf         | Nanum AInMamSonGeurSsi         | 나눔손글씨 아인맘 손글씨    | (주)네이버, 재 네이버문화재단 | OFL             | NAVER CLOVA**** |
| Nanum AJumMaJaYu.ttf               | Nanum AJumMaJaYu               | 나눔손글씨 아줌마 자유      | (주)네이버, 재 네이버문화재단 | OFL             | NAVER CLOVA**** |
| Nanum AmSeuTeReuDam.ttf            | Nanum AmSeuTeReuDam            | 나눔손글씨 암스테르담       | (주)네이버, 재 네이버문화재단 | OFL             | NAVER CLOVA**** |
| Nanum AnSsangCe.ttf                | Nanum AnSsangCe                | 나눔손글씨 안쌍체           | (주)네이버, 재 네이버문화재단 | OFL             | NAVER CLOVA**** |
| Nanum AReumDeuRiGgocNaMu.ttf       | Nanum AReumDeuRiGgocNaMu       | 나눔손글씨 아름드리 꽃나무  | (주)네이버, 재 네이버문화재단 | OFL             | NAVER CLOVA**** |
| Nanum BaeEunHyeCe.ttf              | Nanum BaeEunHyeCe              | 나눔손글씨 배은혜체         | (주)네이버, 재 네이버문화재단 | OFL             | NAVER CLOVA**** |
| Nanum BaegEuiEuiCeonSa.ttf         | Nanum BaegEuiEuiCeonSa         | 나눔손글씨 백의의 천사      | (주)네이버, 재 네이버문화재단 | OFL             | NAVER CLOVA**** |
| Nanum BanJjagBanJjagByeor.ttf      | Nanum BanJjagBanJjagByeor      | 나눔손글씨 반짝반짝 별      | (주)네이버, 재 네이버문화재단 | OFL             | NAVER CLOVA**** |
| Nanum BaReunHiPi.ttf               | Nanum BaReunHiPi               | 나눔손글씨 바른히피         | (주)네이버, 재 네이버문화재단 | OFL             | 눈누***         |
| Nanum BaReunJeongSin.ttf           | Nanum BaReunJeongSin           | 나눔손글씨 바른정신         | (주)네이버, 재 네이버문화재단 | OFL             | NAVER CLOVA**** |
| Nanum BbangGuNiMamSonGeurSsi.ttf   | Nanum BbangGuNiMamSonGeurSsi   | 나눔손글씨 빵구니맘 손글씨  | (주)네이버, 재 네이버문화재단 | OFL             | NAVER CLOVA**** |
| Nanum BeoDeuNaMu.ttf               | Nanum BeoDeuNaMu               | 나눔손글씨 버드나무         | (주)네이버, 재 네이버문화재단 | OFL             | NAVER CLOVA**** |
| Nanum BeomSomCe.ttf                | Nanum BeomSomCe                | 나눔손글씨 범솜체           | (주)네이버, 재 네이버문화재단 | OFL             | NAVER CLOVA**** |
| Nanum BiSangCe.ttf                 | Nanum BiSangCe                 | 나눔손글씨 비상체           | (주)네이버, 재 네이버문화재단 | OFL             | NAVER CLOVA**** |
| Nanum Brush Script.ttf             | Nanum Brush Script             | 나눔손글씨 붓               | (주)네이버, 재 네이버문화재단 | OFL             | 공유마당**      |
| Nanum BugGeugSeong.ttf             | Nanum BugGeugSeong             | 나눔손글씨 북극성           | (주)네이버, 재 네이버문화재단 | OFL             | NAVER CLOVA**** |
| Nanum BuJangNimNunCiCe.ttf         | Nanum BuJangNimNunCiCe         | 나눔손글씨 부장님 눈치체    | (주)네이버, 재 네이버문화재단 | OFL             | NAVER CLOVA**** |
| Nanum CeorPirGeurSsi.ttf           | Nanum CeorPirGeurSsi           | 나눔손글씨 철필글씨         | (주)네이버, 재 네이버문화재단 | OFL             | NAVER CLOVA**** |
| Nanum CoDingHeuiMang.ttf           | Nanum CoDingHeuiMang           | 나눔손글씨 초딩희망         | (주)네이버, 재 네이버문화재단 | OFL             | NAVER CLOVA**** |
| Nanum DaCaeSaRang.ttf              | Nanum DaCaeSaRang              | 나눔손글씨 다채사랑         | (주)네이버, 재 네이버문화재단 | OFL             | NAVER CLOVA**** |
| Nanum DaeGwangYuRi.ttf             | Nanum DaeGwangYuRi             | 나눔손글씨 대광유리         | (주)네이버, 재 네이버문화재단 | OFL             | NAVER CLOVA**** |
| Nanum DaeHanMinGugYeorSaCe.ttf     | Nanum DaeHanMinGugYeorSaCe     | 나눔손글씨 대한민국 열사체  | (주)네이버, 재 네이버문화재단 | OFL             | NAVER CLOVA**** |
| Nanum DaHaengCe.ttf                | Nanum DaHaengCe                | 나눔손글씨 다행체           | (주)네이버, 재 네이버문화재단 | OFL             | NAVER CLOVA**** |
| Nanum DaJinCe.ttf                  | Nanum DaJinCe                  | 나눔손글씨 다진체           | (주)네이버, 재 네이버문화재단 | OFL             | NAVER CLOVA**** |
| Nanum DarEuiGweDo.ttf              | Nanum DarEuiGweDo              | 나눔손글씨 달의궤도         | (주)네이버, 재 네이버문화재단 | OFL             | NAVER CLOVA**** |
| Nanum DaSiSiJagHae.ttf             | Nanum DaSiSiJagHae             | 나눔손글씨 다시 시작해      | (주)네이버, 재 네이버문화재단 | OFL             | NAVER CLOVA**** |
| Nanum DdaAgDanDan.ttf              | Nanum DdaAgDanDan              | 나눔손글씨 따악단단         | (주)네이버, 재 네이버문화재단 | OFL             | NAVER CLOVA**** |
| Nanum DdaDdeusHanJagByeor.ttf      | Nanum DdaDdeusHanJagByeor      | 나눔손글씨 따뜻한 작별      | (주)네이버, 재 네이버문화재단 | OFL             | NAVER CLOVA**** |
| Nanum DdarEGeEomMaGa.ttf           | Nanum DdarEGeEomMaGa           | 나눔손글씨 딸에게 엄마가    | (주)네이버, 재 네이버문화재단 | OFL             | NAVER CLOVA**** |
| Nanum DdoBagDdoBag.ttf             | Nanum DdoBagDdoBag             | 나눔손글씨 또박또박         | (주)네이버, 재 네이버문화재단 | OFL             | NAVER CLOVA**** |
| Nanum DungGeunInYeon.ttf           | Nanum DungGeunInYeon           | 나눔손글씨 둥근인연         | (주)네이버, 재 네이버문화재단 | OFL             | NAVER CLOVA**** |
| Nanum EomMaSaRang.ttf              | Nanum EomMaSaRang              | 나눔손글씨 엄마사랑         | (주)네이버, 재 네이버문화재단 | OFL             | NAVER CLOVA**** |
| Nanum EongGeongKwiCe.ttf           | Nanum EongGeongKwiCe           | 나눔손글씨 엉겅퀴체         | (주)네이버, 재 네이버문화재단 | OFL             | NAVER CLOVA**** |
| Nanum EuiMiIssNeunHanGeur.ttf      | Nanum EuiMiIssNeunHanGeur      | 나눔손글씨 의미있는 한글    | (주)네이버, 재 네이버문화재단 | OFL             | NAVER CLOVA**** |
| Nanum GangBuJangNimCe.ttf          | Nanum GangBuJangNimCe          | 나눔손글씨 강부장님체       | (주)네이버, 재 네이버문화재단 | OFL             | NAVER CLOVA**** |
| Nanum GangInHanWiRo.ttf            | Nanum GangInHanWiRo            | 나눔손글씨 강인한 위로      | (주)네이버, 재 네이버문화재단 | OFL             | NAVER CLOVA**** |
| Nanum GaRamYeonGgoc.ttf            | Nanum GaRamYeonGgoc            | 나눔손글씨 가람연꽃         | (주)네이버, 재 네이버문화재단 | OFL             | NAVER CLOVA**** |
| Nanum GarMaesGeur.ttf              | Nanum GarMaesGeur              | 나눔손글씨 갈맷글           | (주)네이버, 재 네이버문화재단 | OFL             | NAVER CLOVA**** |
| Nanum GeumEunBoHwa.ttf             | Nanum GeumEunBoHwa             | 나눔손글씨 금은보화         | (주)네이버, 재 네이버문화재단 | OFL             | NAVER CLOVA**** |
| Nanum GgeuTeuMeoRiCe.ttf           | Nanum GgeuTeuMeoRiCe           | 나눔손글씨 끄트머리체       | (주)네이버, 재 네이버문화재단 | OFL             | NAVER CLOVA**** |
| Nanum GgocNaeEum.ttf               | Nanum GgocNaeEum               | 나눔손글씨 꽃내음           | (주)네이버, 재 네이버문화재단 | OFL             | NAVER CLOVA**** |
| Nanum GiBbeumBarkEum.ttf           | Nanum GiBbeumBarkEum           | 나눔손글씨 기쁨밝음         | (주)네이버, 재 네이버문화재단 | OFL             | NAVER CLOVA**** |
| Nanum GimYuICe.ttf                 | Nanum GimYuICe                 | 나눔손글씨 김유이체         | (주)네이버, 재 네이버문화재단 | OFL             | NAVER CLOVA**** |
| Nanum GoDigANiGoGoDing.ttf         | Nanum GoDigANiGoGoDing         | 나눔손글씨 고딕 아니고 고딩 | (주)네이버, 재 네이버문화재단 | OFL             | NAVER CLOVA**** |
| Nanum GomSinCe.ttf                 | Nanum GomSinCe                 | 나눔손글씨 곰신체           | (주)네이버, 재 네이버문화재단 | OFL             | NAVER CLOVA**** |
| Nanum GoRyeoGeurGgor.ttf           | Nanum GoRyeoGeurGgor           | 나눔손글씨 고려글꼴         | (주)네이버, 재 네이버문화재단 | OFL             | NAVER CLOVA**** |
| Nanum GyuRiEuiIrGi.ttf             | Nanum GyuRiEuiIrGi             | 나눔손글씨 규리의 일기      | (주)네이버, 재 네이버문화재단 | OFL             | NAVER CLOVA**** |
| Nanum HaengBogHanDoBi.ttf          | Nanum HaengBogHanDoBi          | 나눔손글씨 행복한 도비      | (주)네이버, 재 네이버문화재단 | OFL             | NAVER CLOVA**** |
| Nanum HaNaDoeEoSonGeurSsi.ttf      | Nanum HaNaDoeEoSonGeurSsi      | 나눔손글씨 하나되어 손글씨  | (주)네이버, 재 네이버문화재단 | OFL             | NAVER CLOVA**** |
| Nanum HanYunCe.ttf                 | Nanum HanYunCe                 | 나눔손글씨 한윤체           | (주)네이버, 재 네이버문화재단 | OFL             | NAVER CLOVA**** |
| Nanum HarABeoJiEuiNaNum.ttf        | Nanum HarABeoJiEuiNaNum        | 나눔손글씨 할아버지의나눔   | (주)네이버, 재 네이버문화재단 | OFL             | NAVER CLOVA**** |
| Nanum HaRamCe.ttf                  | Nanum HaRamCe                  | 나눔손글씨 하람체           | (주)네이버, 재 네이버문화재단 | OFL             | NAVER CLOVA**** |
| Nanum HeuiMangNuRi.ttf             | Nanum HeuiMangNuRi             | 나눔손글씨 희망누리         | (주)네이버, 재 네이버문화재단 | OFL             | NAVER CLOVA**** |
| Nanum HeuinGgoRiSuRi.ttf           | Nanum HeuinGgoRiSuRi           | 나눔손글씨 흰꼬리수리       | (주)네이버, 재 네이버문화재단 | OFL             | NAVER CLOVA**** |
| Nanum HimNaeRaNeunMarBoDan.ttf     | Nanum HimNaeRaNeunMarBoDan     | 나눔손글씨 힘내라는 말보단  | (주)네이버, 재 네이버문화재단 | OFL             | NAVER CLOVA**** |
| Nanum HyeJunCe.ttf                 | Nanum HyeJunCe                 | 나눔손글씨 혜준체           | (주)네이버, 재 네이버문화재단 | OFL             | NAVER CLOVA**** |
| Nanum HyeogICe.ttf                 | Nanum HyeogICe                 | 나눔손글씨 혁이체           | (주)네이버, 재 네이버문화재단 | OFL             | NAVER CLOVA**** |
| Nanum HyoNamNeurHwaITing.ttf       | Nanum HyoNamNeurHwaITing       | 나눔손글씨 효남 늘 화이팅   | (주)네이버, 재 네이버문화재단 | OFL             | NAVER CLOVA**** |
| Nanum JaBuSimJiU.ttf               | Nanum JaBuSimJiU               | 나눔손글씨 자부심지우       | (주)네이버, 재 네이버문화재단 | OFL             | NAVER CLOVA**** |
| Nanum JangMiCe.ttf                 | Nanum JangMiCe                 | 나눔손글씨 장미체           | (주)네이버, 재 네이버문화재단 | OFL             | 눈누***         |
| Nanum JarHaGoIssEo.ttf             | Nanum JarHaGoIssEo             | 나눔손글씨 잘하고 있어      | (주)네이버, 재 네이버문화재단 | OFL             | NAVER CLOVA**** |
| Nanum JeomGgorCe.ttf               | Nanum JeomGgorCe               | 나눔손글씨 점꼴체           | (주)네이버, 재 네이버문화재단 | OFL             | NAVER CLOVA**** |
| Nanum JeongEunCe.ttf               | Nanum JeongEunCe               | 나눔손글씨 정은체           | (주)네이버, 재 네이버문화재단 | OFL             | NAVER CLOVA**** |
| Nanum JinJuBagGyeongACe.ttf        | Nanum JinJuBagGyeongACe        | 나눔손글씨 진주 박경아체    | (주)네이버, 재 네이버문화재단 | OFL             | NAVER CLOVA**** |
| Nanum JungHagSaeng.ttf             | Nanum JungHagSaeng             | 나눔손글씨 중학생           | (주)네이버, 재 네이버문화재단 | OFL             | 눈누***         |
| Nanum KarGugSu.ttf                 | Nanum KarGugSu                 | 나눔손글씨 칼국수           | (주)네이버, 재 네이버문화재단 | OFL             | NAVER CLOVA**** |
| Nanum KoKoCe.ttf                   | Nanum KoKoCe                   | 나눔손글씨 코코체           | (주)네이버, 재 네이버문화재단 | OFL             | NAVER CLOVA**** |
| Nanum MasIssNeunCe.ttf             | Nanum MasIssNeunCe             | 나눔손글씨 맛있는체         | (주)네이버, 재 네이버문화재단 | OFL             | NAVER CLOVA**** |
| Nanum MiNiSonGeurSsi.ttf           | Nanum MiNiSonGeurSsi           | 나눔손글씨 미니 손글씨      | (주)네이버, 재 네이버문화재단 | OFL             | NAVER CLOVA**** |
| Nanum MiRaeNaMu.ttf                | Nanum MiRaeNaMu                | 나눔손글씨 미래나무         | (주)네이버, 재 네이버문화재단 | OFL             | NAVER CLOVA**** |
| Nanum MuGungHwa.ttf                | Nanum MuGungHwa                | 나눔손글씨 무궁화           | (주)네이버, 재 네이버문화재단 | OFL             | NAVER CLOVA**** |
| Nanum MuJinJangCe.ttf              | Nanum MuJinJangCe              | 나눔손글씨 무진장체         | (주)네이버, 재 네이버문화재단 | OFL             | NAVER CLOVA**** |
| Nanum NaEuiANaeSonGeurSsi.ttf      | Nanum NaEuiANaeSonGeurSsi      | 나눔손글씨 나의 아내 손글씨 | (주)네이버, 재 네이버문화재단 | OFL             | NAVER CLOVA**** |
| Nanum NaMuJeongWeon.ttf            | Nanum NaMuJeongWeon            | 나눔손글씨 나무정원         | (주)네이버, 재 네이버문화재단 | OFL             | NAVER CLOVA**** |
| Nanum NaNeunIGyeoNaenDa.ttf        | Nanum NaNeunIGyeoNaenDa        | 나눔손글씨 나는 이겨낸다    | (주)네이버, 재 네이버문화재단 | OFL             | NAVER CLOVA**** |
| Nanum NeuRisNeuRisCe.ttf           | Nanum NeuRisNeuRisCe           | 나눔손글씨 느릿느릿체       | (주)네이버, 재 네이버문화재단 | OFL             | 눈누***         |
| Nanum NoRyeogHaNeunDongHeui.ttf    | Nanum NoRyeogHaNeunDongHeui    | 나눔손글씨 노력하는 동희    | (주)네이버, 재 네이버문화재단 | OFL             | NAVER CLOVA**** |
| Nanum OeHarMeoNiGeurSsi.ttf        | Nanum OeHarMeoNiGeurSsi        | 나눔손글씨 외할머니글씨     | (주)네이버, 재 네이버문화재단 | OFL             | 눈누***         |
| Nanum OenSonJabIDoYeBbeo.ttf       | Nanum OenSonJabIDoYeBbeo       | 나눔손글씨 왼손잡이도 예뻐  | (주)네이버, 재 네이버문화재단 | OFL             | NAVER CLOVA**** |
| Nanum OgBiCe.ttf                   | Nanum OgBiCe                   | 나눔손글씨 옥비체           | (주)네이버, 재 네이버문화재단 | OFL             | NAVER CLOVA**** |
| Nanum Pen Script.ttf               | Nanum Pen Script               | 나눔손글씨 펜               | (주)네이버, 재 네이버문화재단 | OFL             | 공유마당**      |
| Nanum SangHaeCanMiCe.ttf           | Nanum SangHaeCanMiCe           | 나눔손글씨 상해찬미체       | (주)네이버, 재 네이버문화재단 | OFL             | NAVER CLOVA**** |
| Nanum SaRangHaeADeur.ttf           | Nanum SaRangHaeADeur           | 나눔손글씨 사랑해 아들      | (주)네이버, 재 네이버문화재단 | OFL             | NAVER CLOVA**** |
| Nanum SeACe.ttf                    | Nanum SeACe                    | 나눔손글씨 세아체           | (주)네이버, 재 네이버문화재단 | OFL             | NAVER CLOVA**** |
| Nanum SeGyeJeogInHanGeur.ttf       | Nanum SeGyeJeogInHanGeur       | 나눔손글씨 세계적인 한글    | (주)네이버, 재 네이버문화재단 | OFL             | NAVER CLOVA**** |
| Nanum SeHwaCe.ttf                  | Nanum SeHwaCe                  | 나눔손글씨 세화체           | (주)네이버, 재 네이버문화재단 | OFL             | NAVER CLOVA**** |
| Nanum SeongSirCe.ttf               | Nanum SeongSirCe               | 나눔손글씨 성실체           | (주)네이버, 재 네이버문화재단 | OFL             | NAVER CLOVA**** |
| Nanum SinHonBuBu.ttf               | Nanum SinHonBuBu               | 나눔손글씨 신혼부부         | (주)네이버, 재 네이버문화재단 | OFL             | NAVER CLOVA**** |
| Nanum SiUGwiYeoWeo.ttf             | Nanum SiUGwiYeoWeo             | 나눔손글씨 시우 귀여워      | (주)네이버, 재 네이버문화재단 | OFL             | NAVER CLOVA**** |
| Nanum SoBangGwanEuiGiDo.ttf        | Nanum SoBangGwanEuiGiDo        | 나눔손글씨 소방관의 기도    | (주)네이버, 재 네이버문화재단 | OFL             | NAVER CLOVA**** |
| Nanum SoMiCe.ttf                   | Nanum SoMiCe                   | 나눔손글씨 소미체           | (주)네이버, 재 네이버문화재단 | OFL             | NAVER CLOVA**** |
| Nanum SonPyeonJiCe.ttf             | Nanum SonPyeonJiCe             | 나눔손글씨 손편지체         | (주)네이버, 재 네이버문화재단 | OFL             | NAVER CLOVA**** |
| Nanum URiDdarSonGeurSsi.ttf        | Nanum URiDdarSonGeurSsi        | 나눔손글씨 우리딸 손글씨    | (주)네이버, 재 네이버문화재단 | OFL             | NAVER CLOVA**** |
| Nanum WaIrDeu.ttf                  | Nanum WaIrDeu                  | 나눔손글씨 와일드           | (주)네이버, 재 네이버문화재단 | OFL             | NAVER CLOVA**** |
| Nanum YaCaeJangSuBaegGeumRye.ttf   | Nanum YaCaeJangSuBaegGeumRye   | 나눔손글씨 야채장수 백금례  | (주)네이버, 재 네이버문화재단 | OFL             | NAVER CLOVA**** |
| Nanum YaGeunHaNeunGimJuIm.ttf      | Nanum YaGeunHaNeunGimJuIm      | 나눔손글씨 야근하는 김주임  | (주)네이버, 재 네이버문화재단 | OFL             | NAVER CLOVA**** |
| Nanum YeBbeunMinGyeongCe.ttf       | Nanum YeBbeunMinGyeongCe       | 나눔손글씨 예쁜 민경체      | (주)네이버, 재 네이버문화재단 | OFL             | NAVER CLOVA**** |
| Nanum YeDangCe.ttf                 | Nanum YeDangCe                 | 나눔손글씨 예당체           | (주)네이버, 재 네이버문화재단 | OFL             | NAVER CLOVA**** |
| Nanum YeonJiCe.ttf                 | Nanum YeonJiCe                 | 나눔손글씨 연지체           | (주)네이버, 재 네이버문화재단 | OFL             | 눈누***         |
| Nanum YeorAHobEuiBanJjagIm.ttf     | Nanum YeorAHobEuiBanJjagIm     | 나눔손글씨 열아홉의 반짝임  | (주)네이버, 재 네이버문화재단 | OFL             | NAVER CLOVA**** |
| Nanum YeoReumGeurSsi.ttf           | Nanum YeoReumGeurSsi           | 나눔손글씨 여름글씨         | (주)네이버, 재 네이버문화재단 | OFL             | NAVER CLOVA**** |
| Nanum YeorIrCe.ttf                 | Nanum YeorIrCe                 | 나눔손글씨 열일체           | (주)네이버, 재 네이버문화재단 | OFL             | NAVER CLOVA**** |
| Nanum YuNiDdingDdangDdingDdang.ttf | Nanum YuNiDdingDdangDdingDdang | 나눔손글씨 유니 띵땅띵땅    | (주)네이버, 재 네이버문화재단 | OFL             | NAVER CLOVA**** |
| NanumBarunGothic.ttf               | NanumBarunGothic               | 나눔바른고딕                | (주)네이버, 재 네이버문화재단 | OFL             | 공유마당**      |
| NanumBarunpen.ttf                  | NanumBarunpen                  | 나눔바른펜                  | (주)네이버, 재 네이버문화재단 | OFL             | 공유마당**      |
| NanumGothic.ttf                    | NanumGothic                    | 나눔고딕                    | (주)네이버, 재 네이버문화재단 | OFL             | 공유마당**      |
| NanumMyeongjo.ttf                  | NanumMyeongjo                  | 나눔명조                    | (주)네이버, 재 네이버문화재단 | OFL             | 눈누***         |
| NeoDunggeunmo.ttf                  | NeoDunggeunmo                  | Neo둥근모                   | Dalgona                       | OFL             | 눈누***         |
| PureBatang Medium.ttf              | PureBatang Medium              | 순바탕 Medium               | 한국출판문화산업진흥원        | 공공누리 1유형* | 공유마당**      |
| PureunJeonnam.ttf                  | PureunJeonnam                  | 푸른전남                    | 전라남도                      | 공공누리 1유형* | 공유마당**      |
| Samgukji Korean Font.ttf           | Samgukji Korean Font           | 삼국지3글꼴                 | leedheo                       | MIT             | 눈누***         |
| SeoulHangang.ttf                   | SeoulHangang B                 | 서울한강체 B                | 서울시                        | 공공누리 1유형* | 공유마당**      |
| SeoulNamsan.ttf                    | SeoulNamsan B                  | 서울남산체 B                | 서울시                        | 공공누리 1유형* | 공유마당**      |
| Spoqa Han Sans Neo Regular.ttf     | Spoqa Han Sans Neo Regular     | 스포카 한 산스 R            | 스포카                        | OFL             | 눈누***         |
| SpoqaHanSans-Regular.ttf           | SpoqaHanSans-Regular           | 스포카 한 산스 R            | 스포카                        | OFL             | 공유마당**      |
| Suncheon R.ttf                     | Suncheon R                     | 순천 R                      | 순천시                        | 공공누리 1유형* | 공유마당**      |
| TmonMonsori Black.ttf              | TmonMonsori Black              | Tmon몬소리 Black            | 티몬                          | OFL             | 눈누***         |
| UNPEOPLE Gothic UNI.ttf            | UNPEOPLE Gothic UNI            | 유앤피플 고딕 UNI           | (주)유앤피플                  | OFL             | 공유마당**      |
| Wandocleansea.ttf                  | Wandocleansea                  | 완도청정바다체              | 완도군                        | 공공누리 1유형* | 공유마당**      |
| YangPyeong M.ttf                   | YangPyeong M                   | 양평군체 M                  | 양평군                        | 공공누리 1유형* | 공유마당**      |

### Reference
\* 공공누리 1유형: [여기](https://www.kogl.or.kr/info/license.do#01-tab)를 참고하세요.  
\*\* 공유마당 : https://gongu.copyright.or.kr/gongu/bbs/B0000018/list.do?menuNo=200195  
\*\*\* 눈누: https://noonnu.cc/  
\*\*\*\* NAVER CLOVA: https://clova.ai/handwriting/list.html

### Reference (English)
\* 공공누리 1유형(KOGL - Korean Open Goverment License, "Gonggongnuri" Type 1): Please refer [here](https://www.kogl.or.kr/info/license.do#05-tab) to get more information.  
\*\* 공유마당 : https://gongu.copyright.or.kr/gongu/bbs/B0000018/list.do?menuNo=200195  
\*\*\* 눈누: https://noonnu.cc/  
\*\*\*\* NAVER CLOVA: https://clova.ai/handwriting/list.html