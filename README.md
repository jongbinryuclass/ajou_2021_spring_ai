# [2021 Spring Class] Ajou AI by JBR
1. **대회목표**: 
   
   팀별로 Query data와 가장 가까운 Gallery data를 찾는 인공지능 만들기
   
   주어진 train data와 train label을 이용하여 Query data와 가장 가까운 Gallery data의 index에 해당하는 class label을 github에 제출

2. **세부 프로토콜**

   원본데이터셋: CUB200 datasets

   실습데이터셋: https://drive.google.com/drive/folders/1ItDbPIEkkQ2P2OvB1xg728tNB1NvCXkA?usp=sharing
   
   네트워크 파라미터: 제한없음

   아키텍쳐: 제한없음

   학습알고리즘: 제한없음

   딥러닝 프레임워크: PyTorch, TensorFlow 권장, 다른 프레임워크도 사용 가능

3. **순위산정:** 이미지 데이터셋의 Top-1 Accuracy

4. **팀 구성**: 사전 5인으로 구성된 팀

5. **제출데이터**: nearest neighbor data의 index에 해당하는 class label (github에 제출) + 각 Probe data 별 Gallery data의 distance (email 제출) #num_of_probe_data * #num_of_gallery_data

6. **대회진행**

   |     날짜      |      일정       |
   | :-----------: | :-------------: |
   |     시작      | 2021년 3월 24일 |
   |     중간      | 2021년 5월 21일 |
   |     기말      | 2021년 6월 15일 |
   | 최종결과 발표 | 2021년 6월 22일 |

7. **최종 결과 산출 방법:** 중간, 기말 시점의 정확도를 일정 비율로 합쳐서 최종 결과에 반영

8. **거리(distance)값 제출:** 중간, 기말 시점의 팀별로 구축한 모델의 "각 Probe data 별 Gallery data의 distance"를 저장하여(kimsungeun@ajou.ac.kr) 메일로 제출

## 퍼블릭 랭킹

  
- Total Score가 아직 업데이트되지 않았습니다. 
 - 다음 업데이트 일정은 중간 점수 집계(2021-05-21) 입니다.
  
**현재 랭킹 1위는 team8 입니다. 평균 accuracy는 4.67% 입니다.**
|Ranking|Name|Penalty|Accuracy(%)|Last Submission|Total Submission Count|Total Score(%)|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|1|team8|0|5.8|2021-05-14 22:24:31.747631+09:00|41|0.0|
|2|team7|0|5.5|2021-05-14 19:16:12.645231+09:00|22|0.0|
|3|team4|0|5.4|2021-05-15 19:36:01.868996+09:00|20|0.0|
|4|team1|0|5.1|2021-05-16 20:52:51.788905+09:00|37|0.0|
|5|team5|0|5.0|2021-05-15 01:08:53.839644+09:00|7|0.0|
|6|team10|0|5.0|2021-05-15 02:01:46.970566+09:00|14|0.0|
|7|team13(auditor)|0|4.9|2021-05-14 15:56:32.168183+09:00|33|0.0|
|8|team2|0|4.9|2021-05-16 23:34:12.889812+09:00|44|0.0|
|9|team12|0|4.7|2021-05-15 06:16:57.542125+09:00|18|0.0|
|10|team6|0|4.7|2021-05-16 20:52:51.788905+09:00|4|0.0|
|11|team3|0|4.7|2021-05-16 23:51:05.480916+09:00|19|0.0|
|12|professor|0|3.4|2021-05-07 13:14:30.576267+09:00|5|0.0|
|13|team9|0|3.2|2021-05-14 15:24:37.050328+09:00|4|0.0|
|14|team11|0|3.1|2021-05-14 21:41:47.198305+09:00|11|0.0|


**정확도는 소숫점 5자리 까지 출력됩니다.**
**Time zone is seoul,korea (UTC+9:00)**
## 퍼블릭 랭킹 제출 방법

팀별로 구성한 모델의 테스트 데이터 셋을 예측한 결과값을 `Encrypt.py` 를 이용해 암호화하여 `submission` 폴더의 해당 팀 폴더에 제출합니다.

**주의사항** : 

1. 제출 파일명은 자유롭게 작성 할 수 있습니다.(단, 폴더당 하나의 파일만 존재해야 합니다. 그렇지 않을 경우 채점이 되지 않습니다.)
2. `.github` 폴더는 건들지 않도록 합니다.
3. 총 100회 까지 제출할 수 있고 이 이상 제출해도 채점 되지 않습니다.

Example) Team1인 경우 제출 방법

1. 예측 파일 만들기. 다음과 같은 예측 파일이 있다고 가정합니다. (query 데이터에 대한 예측 결과 파일)

   `ans.txt` 예시

   ```tex
   9
   8
   10
   99
   98
   70
   18
   33
   ```
   
2. 예측 파일(`ans.txt`)과 전달받은 키를 `Encrypt` 폴더에 넣고 `Encrypt.py`를 실행 시켜서 암호화한 예측 파일(`ans.json`)을 생성합니다. 
생성한 파일을 (`submission/team1`)에 넣고 commit 후 push 를 실행하면 완료됩니다.

   ```python
   # 1.이메일을 통해서 전달 받은 키 파일의 경로 입력
   key_path = "key.pem"
   # 2. 예측한 결과를 텍스트 파일로 저장했을 경우 리스트로 다시 불러오기
   # 본인이 원하는 방식으로 리스트 형태로 예측 값을 불러오기만 하면 됨(순서를 지킬것)
   raw_ans_path = "ans.txt"
   ans = read_txt(raw_ans_path)
   # 3. 암호화된 파일을 저장할 위치
   encrypt_ans_path = "../submission/team1/ans.json"
   # 4. 암호화!(pycrytodome 설치)
   encrypt_data(key_path, ans, encrypt_ans_path)
   ```
   

이 때 꼭 로컬에서 이 스크립트를 실행해서 제출하지 않고 코랩에서 pycryptodomex 라이브러리를 설치한 후 스크립트 실행시켜서 정답 파일 만든 뒤에 제출해도 무방합니다.



## 퍼블릭 랭킹 평가 방법

query 데이터에 대한 예측값의 정확도가 퍼블릭 랭킹에 그대로 반영됩니다.

ex) `ans.txt`=(query 데이터에 대한 예측값), top 1 acc = 98%

```tex
9
8
10
99
98
70
18
33
```



## 암호화 모듈 설치 방법

설치 방법 설명은 [공식 문서](https://pycryptodome.readthedocs.io/en/latest/src/installation.html#windows-from-sources-python-3-5-and-newer)에 잘 나와있습니다. 아래 내용은 공식 문서에서 나온 내용을 가져왔습니다. 

파이썬 3.5 이상, 윈도우에서 Pycryptodomex 설치하는 방법

1. **[Once only, C Compiler가 미설치 되어있는 경우에만]** Download [Build Tools for Visual Studio 2019](https://visualstudio.microsoft.com/downloads/#build-tools-for-visual-studio-2019). In the installer, select the *C++ build tools*, the *Windows 10 SDK*, and the latest version of *MSVC v142 x64/x86 build tools*.

2. Compile and install PyCryptodome:

   ```
   > pip install pycryptodomex --no-binary :all:
   ```

3. To make sure everything work fine, run the test suite:

   ```
   > python -m Cryptodome.SelfTest
   ```



문의사항이 있으신 분은 kimsungeun@ajou.ac.kr 로 문의주시길 바랍니다.
