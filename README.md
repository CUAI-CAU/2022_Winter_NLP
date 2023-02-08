# 2022_Winter_NLP
## 2022 CUAI Winter Conference NLP Team Repository

### 👨💻 팀원
* 김민기 (경영학부)
* 김민주 (경영학부)
* 김지민 (응용통계학과)
* 이혜연 (응용통계학과)

### :pushpin: opic
<hr/>
브로카 실어증 치료를 위한 서비스 구현 (Implementation of services to treat Broca aphasia)

### :point_right: Summary
<hr/>
본 연구는 브로카 실어증 환자들이 보호자 없이도 꾸준한 언어치료를 할 수 있도록 하는 것을 목적으로 대화형 언어 치료 모델을 활용한 서비스를 제안함. 

서비스는 낱말 이름 맞히기, 이미지 보고 체언과 용언 맞히기, 시스템과 대화 나누기의 3단계의 과정이 STT 기술과 MLM 모델을 사용해서 구성됨. 

-> BDU 모델 : 3단계에서 사용한 BDU라는 MLM모델은 KoElectra를 활용하여 개발됨. 이를 통해 브로카 실어증 환자가 문법형태소가 생략된 발화시 완전한 문장을 출력하여 실문법증 치료에 도움이 되도록 함.

### :point_right: Our goal
<hr/>
브로카 실어증 환자들이 보호자 없이도 꾸준한 언어치료를 할 수 있도록 도움을 제공한다.

### :point_right: Meeting Log
<hr/>

| 날짜 | 내용 |
|---|---|
| 22.12.26 | 주제 회의 |  
| 23.01.05 | 주제 확정, 연구 배경 및 관련 데이터셋 탐색 |
| 23.01.09 | MLM 모델 탐색 |
| 23.01.14 | 모델 세부 기능 논의 |
| 23.01.17 | 서비스의 프로토타입 방향 설정 |
| 23.01.20 | 서비스에 필요한 각종 데이터 수집 |
| 23.01.31 | 모델 파인튜닝 및 데이터 전처리 |
| 23.02.02 | 코드 및 자료 정리 |
| 23.02.04 | 숏페이퍼, 포스터, PPT, 대본 역할 분담 및 준비 |

### :point_right: Framework
<hr/>

* Level 1

![1단계](https://user-images.githubusercontent.com/100768412/217162955-47f8f98c-3ee4-4269-8e39-b05ad947cf50.PNG)

* Level 2

![2단계](https://user-images.githubusercontent.com/100768412/217162963-4b6775a9-b990-4128-a56a-17ee68455817.PNG)

* Level 3

![3단계](https://user-images.githubusercontent.com/100768412/217162985-c70da71a-3da3-4499-a2fd-735697300ef6.PNG)

### :point_right: example of Result
<hr/>

![KakaoTalk_20230207_143120850](https://user-images.githubusercontent.com/100768412/217163256-a0bd7857-ff1e-4abd-9a76-b5f3756aa3d5.png)

