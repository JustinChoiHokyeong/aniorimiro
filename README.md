# 용산구 상권분석 및 매출예측 서비스 프로젝트
* 참여자 : 최호경, 김신혜, 민현진, 윤현성, 정다정, 최현호 (6명)
* 총 개발기간 : 2022/11/26 ~ 2022/12/26 (4주) 

## 목차
* [회의록](#회의록)
* [프로젝트 문서](#프로젝트-문서) 
* [사용 데이터](#사용-데이터)
* [프로젝트 개요](#프로젝트-개요)
* [데이터 분석 과정](#데이터-분석-과정)
* [웹 개발 과정](#웹-개발-과정)
* [사용 방법(동작법)](#사용-방법동작법)
* [미래 개선 방안](#미래-개선-방안)
* [Skills](#skills)
* [참조 사이트](#참조-사이트)
 

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
4. [covid19/서울시 코로나19 자치구별 확진자 발생동향.csv](https://github.com/JustinChoiHokyeong/aniorimiro/blob/master/aniorimiro/static/data/covid/%EC%84%9C%EC%9A%B8%EC%8B%9C%20%EC%BD%94%EB%A1%9C%EB%82%9819%20%EC%9E%90%EC%B9%98%EA%B5%AC%EB%B3%84%20%ED%99%95%EC%A7%84%EC%9E%90%20%EB%B0%9C%EC%83%9D%EB%8F%99%ED%96%A5.csv)
5. [covid19/서울시 코로나19 확진자 발생동향.csv](https://github.com/JustinChoiHokyeong/aniorimiro/blob/master/aniorimiro/static/data/covid/%EC%84%9C%EC%9A%B8%EC%8B%9C%20%EC%BD%94%EB%A1%9C%EB%82%9819%20%ED%99%95%EC%A7%84%EC%9E%90%20%EB%B0%9C%EC%83%9D%EB%8F%99%ED%96%A5.csv)
6. [서울시 우리마을가게 상권분석서비스 상권영역 4개 유형 꼭짓점 좌표 데이터(TBGIS_TRDAR_RELM.shp)](https://data.seoul.go.kr/dataList/OA-15560/S/1/datasetView.do)


## 프로젝트 개요
#### 1. 프로젝트명 : aniorimiro (아니오리미로)
#### 2. 주제 : 용산구 상권분석 및 매출예측 서비스
#### 3. 목적 및 배경 : 
--------프로젝트 제작 배경 및 이유 보완해서 적기 ----------
> 의사결정에 도움을 줄 수 있는 다양한 상권분석 정보를 제공하여, 상권활성화 및 예비창업을 지원하기 위함


## 데이터 분석 과정
### 1. 데이터 탐색 및 전처리
* 변수 정의
* 탐색 시각화 자료

### 2. 모델링

## 웹 개발 과정
### 1. 장고
#### 1) settings.py 세팅 
> templates와 static을 각각 BASE_DIR 경로를 정해줘서 상위 폴더로 한번에 모아놓고 참조해서 사용할 수 있도록 구성함. 
>> templates에서는 html파일들을 accounts, analysis, etc, index로 기능별로 분류하여 저장. 
>> static 폴더 안에 css, data, pictures로 분류하여 정적 데이터 저장 
``` python
'DIRS': [os.path.join(BASE_DIR, 'templates')],
```
``` python
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
```
> MariaDB 데이터베이스 연결
``` python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '4team',
        'USER' : 'root',
        'PASSWORD': '비밀번호',
        'HOST' : '61.74.225.3',
        'PORT':'3306',
    }
}
DATABASE_OPTIONS = {'charset': 'utf-8'} 
```

#### 2) 로그인, 로그아웃, 회원가입, 마이페이지 기능 구현
> Django auth에 내장된 views, forms, models 기능를 사용하여 간단한 계정 관련 기능을 구현하였음.
``` python
#accounts/urls.py
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('login/', LoginView.as_view(template_name='accounts/login.html'),name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profile/update/', views.update, name='update'),
    path('signup/', views.signup, name='signup'),
    path('', views.index, name='index'), 
]
```
> auth.models의 User 테이블과 자체 field을 활용하고, forms.py를 만든 후 마찬가지로 장고의 auth forms에 있는 폼을 사용하여 회원가입, 마이페이지, 사용자 정보 수정 기능을 구현함.
``` python
#accounts/forms.py
from django import forms
from .models import Profile
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

class ProfileForm(forms.ModelForm):
  class Meta:
    model = Profile
    fields = ['email_is_agreed']

class CreateUserForm(UserCreationForm):
  email = forms.EmailField(required=True)
  first_name = forms.CharField(max_length=50)
  last_name = forms.CharField(max_length=50)

  class Meta:
    model = User
    fields = ("username", "password1", "password2", "email", "first_name", "last_name")

  def save(self, commit=True):
    user = super(CreateUserForm, self).save(commit=False)
    user.email = self.cleaned_data["email"]
    user.first_name = self.cleaned_data["first_name"]
    user.last_name = self.cleaned_data["last_name"]
    if commit:
      user.save()
    return user

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name','last_name']
```


### 2. 카카오 지도 API
#### 1) 
#### 2) 
#### 3) 공부해서 다른 조에게 공유했던 점
#### 4) 외부 CSS 파일로 한번에 정리 

### 3. JQuery Ajax 데이터 전달
------- 예전 플젝에서 보완해서 연구해서 업그레이드 --------
제이슨 공부해서 쓴거


## 사용 방법(동작법) 

## 미래 개선 방안

### 1. 데이터 분석
#### 1) 분석결과 시각화?

### 2. 웹 개발
#### 1) 마이페이지 스크랩 저장 기능
#### 2) 인포윈도우 -> 커스텀 오버레이로 수정
3) AWS 클라우드 서버 출력




## Skills
* **OS** : Windows, MacOS
* **Language** : Python, HTML5, CSS3, JavaScript(ES6)
* **Framework/Library** : Django, jQurey, Pandas, SciPy, -------데이터에서 사용한 라이브러리 추가하기--------
* **Database** : MariaDB
* **IDE** : Eclipse, VS Code
* **Collaboration** : GitHub, Slack, Discord, Google Sheets

## 참조 사이트
1. [우리마을가게 상권분석서비스](https://golmok.seoul.go.kr/main.do)
2. [소상공인마당 상권정보](https://sg.sbiz.or.kr/godo/index.sg)
3. [카카오 지도 API](https://apis.map.kakao.com/web/)
4. [shp 파일 영역좌표 추출 사이트(QGIS)](https://www.qgis.org/ko/site/)
5. [JSON 파일 유효성 검증 사이트](https://jsonlint.com/)

