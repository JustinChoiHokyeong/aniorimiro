# 용산구 상권분석 및 매출예측 서비스 프로젝트
* 참여자 : 최호경, 김신혜, 민현진, 윤현성, 정다정, 최현호 (6명)
* 총 개발기간 : 2022/11/26 ~ 2022/12/26 (4주)

## 회의록
1. [팀장 회의 - 팀 선정 및 프로젝트 설명](https://justdojustin.tistory.com/50)
2. [1차 회의록 - 데이터 및 주제 선정](https://justdojustin.tistory.com/51)
3. [2차 회의록 - 세부 주제 선정 및 역할 분담](https://justdojustin.tistory.com/52)
4. [3차 회의록 - 기능정의서 작성 및 세부 계획 수립](https://justdojustin.tistory.com/53)
5. [5차 회의록 - 화면정의서 작성 및 데이터 탐색](https://justdojustin.tistory.com/54)
6. [1차 멘토링 피드백 - WBS 작성 및 세부 기능 구현](https://justdojustin.tistory.com/55)
7. [프로젝트 중간 점검 회의록 - 프로젝트 진행현황 점검](https://justdojustin.tistory.com/56)
8. [2차 멘토링 피드백 - AWS 클라우드 서버 출력 시도](https://justdojustin.tistory.com/57)
9. [3차 멘토링 피드백 - 작동 테스트 및 피드백 개선](https://justdojustin.tistory.com/58)

## 프로젝트 문서
* [기능정의서](https://docs.google.com/spreadsheets/d/167e_ifRUj6Zdcu5U6ka96ypv0CCr_WbWnllNXcaQBX0/edit#gid=0)
* [화면정의서](https://docs.google.com/presentation/d/1YypgBo2MCVdZVHRleeFGBvraXvuPCPOf4g5z-fwrZg0/edit#slide=id.p)
* [WBS(Work Breakdown Structure)](https://docs.google.com/spreadsheets/d/1DsW8wfOfBu1VqastvK6YuBT5czBZfACZJwIsM4Kl9CA/edit#gid=0)
* [발표 PPT (K-Digital Training 양식)](https://docs.google.com/presentation/d/1JeNPFPwV64P2TyMtRyJBHAofCZ2TNr_g/edit?usp=sharing&ouid=112815532964849845221&rtpof=true&sd=true)

## 사용 데이터
1. [서울시_우리마을가게_상권분석서비스(신_상권_추정매출)_2019년.csv](https://data.seoul.go.kr/dataList/OA-15572/S/1/datasetView.do)
2. [서울시_우리마을가게_상권분석서비스(신_상권_추정매출)_2020년.csv](https://data.seoul.go.kr/dataList/OA-15572/S/1/datasetView.do)
3. [서울시_우리마을가게_상권분석서비스(신_상권_추정매출)_2021년.csv](https://data.seoul.go.kr/dataList/OA-15572/S/1/datasetView.do)
4. [서울시 우리마을가게 상권분석서비스 상권영역 4개 유형 꼭짓점 좌표 데이터(TBGIS_TRDAR_RELM.shp)](https://data.seoul.go.kr/dataList/OA-15560/S/1/datasetView.do)


## 프로젝트 개요
#### 1. 프로젝트명 : aniorimiro (아니오리미로)
#### 2. 주제 : 용산구 상권분석 및 매출예측 서비스
#### 3. 목적 및 배경 : 
> 의사결정에 도움을 줄 수 있는 다양한 상권분석 정보를 제공하여, 상권활성화 및 예비창업을 지원하기 위함

## 데이터 분석 과정
#### 1. 데이터 탐색 및 전처리
* 변수 정의
* 탐색 시각화 자료

#### 2. 모델링

## 웹 개발 과정
### 1. 장고(로그인, 회원가입, 마이페이지)
#### 1) settings.py 기본 
> templates에는 static 폴더 안에 css, data, pictures 폴더를 만듬 -> 각각 root 루트 경로를 정해줘서 한번에 모아놓고 참조해서 사용할 수 있도록 구성
``` 
'DIRS': [os.path.join(BASE_DIR, 'templates')],
```
```
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
```
#### 2. 카카오 지도 API

#### 3. JQuery Ajax 데이터 전달



## 차후 개선 방향성
#### 1. 마이페이지 스크랩 저장 기능
#### 2. 인포윈도우 -> 커스텀 오버레이로 수정
#### 3. 분석결과 시각화?

## 전체 코드

## 참조 사이트
1. [우리마을가게 상권분석서비스](https://golmok.seoul.go.kr/main.do)
2. [소상공인마당 상권정보](https://sg.sbiz.or.kr/godo/index.sg)
3. [카카오 지도 API](https://apis.map.kakao.com/web/)
4. [shp 파일 영역좌표 추출 사이트(QGIS)](https://www.qgis.org/ko/site/)
5. [JSON 파일 유효성 검증 사이트](https://jsonlint.com/)

