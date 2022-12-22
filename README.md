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


### 2. 지도 기능 구현
#### 1) 카카오 지도 API 사용
> 지도 상에서 유용하게 사용할 수 있는 다양한 기능을 html+javascript sample 코드를 제공한다. 이를 기반으로 하고, JavaScript와 jQuery를 사용하여 아래와 같은 기능을 구현했다.
1. 상권 영역 독립적으로 출력 및 클릭 가능
<img width="387" alt="Screen Shot 2022-12-22 at 8 34 05 PM" src="https://user-images.githubusercontent.com/108642193/209125799-e8369476-8d3c-4ea6-a6d1-7d82d7ad07fa.png">

> 새로운 빈 배열을 상권별로 생성

```javascript 
let areas_gm = new Array();
let areas_gg = new Array();
let areas_bd = new Array();
let areas_jt = new Array();
```

> 제이쿼리를 사용해서 스태틱 폴더에 저장된 json 파일을 불러오고, 상권별로 각각의 변수에 담아줌

```javascript 
let jsonLoca_gm = '/static/data/gm.json';
let jsonLoca_gg = '/static/data/gg.json';
let jsonLoca_bd = '/static/data/bd.json';
let jsonLoca_jt = '/static/data/jt.json';
```


2. hover 버튼을 통해 4개 유형 중에 1개씩만 출력
<img width="366" alt="Screen Shot 2022-12-22 at 8 41 19 PM" src="https://user-images.githubusercontent.com/108642193/209126986-19d8da5e-a9f7-4171-8b9e-e5eef3dfb005.png">

> setComArea 함수를 만들어 클릭할 때 해당 id를 가진 요소 버튼의 클래스를 변경하여 클릭된 형태의 css가 적용되게 했다. 그리고 클릭 시 서로 다른 매개변수가 함수에 전달되게 했다.

```javascript
//javacript
function setComArea(areatype){
  let bdControl = document.getElementById('btnBd');
  let ggControl = document.getElementById('btnGg');
  let gmControl = document.getElementById('btnGm');
  let jtControl = document.getElementById('btnJt');
  
//html
<div class="areacontrol radius_border">
    <span id="btnGm" class="btn" onclick="setComArea('gm')">골목상권</span>
    <span id="btnGg" class="btn" onclick="setComArea('gg')">관광특구</span>
    <span id="btnBd" class="btn" onclick="setComArea('bd')">발달상권</span>
    <span id="btnJt" class="btn" onclick="setComArea('jt')">전통시장</span>    
</div> 

```

> if문을 통해 매개변수에 따라 각각 다른 영역이 생성되게 하였고, 호버 버튼이기 때문에 다른 버튼을 또 누르면 기존의 지도는 삭제되게 만들었다. 구체적인 과정은 코드의 주석을 참조.

```javascript
if(areatype === 'bd'){
    //기존의 그려져있던 영역 삭제하고
    $("path").remove();
    //새로운 영역 그리기
    //lineColor : 2838F2
    $.getJSON(jsonLoca_bd, function(data){
      //반복문 돌면서 상권별 데이터를 담을 준비
      $.each(data, function(I, item){
          //상권명과 좌표정보를 담을 객체를 생성하고 {}
          let area = new Object();
          //상권명은 바로 name이라는 키값에 전달한다 name:""
          area.name = item.name;
          //좌표정보는 path라는 키값에 전달할건데
          //우선 새로운 배열을 생성해서
          area.path = new Array();
          //for문을 이용해 돌면서 좌표정보를 담을 것이다
          for (let i=0; i<item.LatLng.length; i++){
            //위에서 제이쿼리 each 반복문에서 가져온 위도경도 값을 카카오 LatLng 메소드에 넣고
            //생성된 객체를 newlatlng 변수에 담았다
            let newlatlng = new kakao.maps.LatLng(item.LatLng[i][0], item.LatLng[i][1])
            //그리고 area라는 배열에 반복문을 돌면서 담았다
            area.path.push(newlatlng)
          }        
          //담은 name과 path를 모두 담은 객체는 areas 배열에 each 반복문을 돌면서 push로 추가시킨다.
          areas_bd.push(area);
      })
      //for 반복문을 돌면서 displayArea 메소드를 사용해서 상권 영역을 지도에 그린다.
      for (var i = 0, len = areas_bd.length; i < len; i++) {
        displayArea(areas_bd[i], '#2838F2');
    }});
    bdControl.className = "selected_btn";
    ggControl.className = "btn";
    gmControl.className = "btn";
    jtControl.className = "btn";

  }
```



4. 마우스 오버 시, 상권명 표시 및 내부색 활성화
<img width="329" alt="Screen Shot 2022-12-22 at 8 12 51 PM" src="https://user-images.githubusercontent.com/108642193/209122504-9f21a82d-3b0f-4521-960e-ddee0450923e.png">

```javascript 
kakao.maps.event.addListener(polygon, 'mouseover', function(mouseEvent) {
        polygon.setOptions({fillColor: '#09f'});

        customOverlay.setContent('<div class="area">' + area.name + '</div>');
        
        customOverlay.setPosition(mouseEvent.latLng); 
        customOverlay.setMap(map);
    });
```

3. 상권영역 클릭 시 인포윈도우 출력하여 상권명, 영역 넓이 확인 가능 + 클릭 위치를 중심 좌표로 포커싱
<img width="279" alt="Screen Shot 2022-12-22 at 8 22 21 PM" src="https://user-images.githubusercontent.com/108642193/209123892-5650e7c0-5fb3-4d4c-8d61-790d195cb2b4.png">

```javascript 
// 다각형에 click 이벤트를 등록하고 이벤트가 발생하면 다각형의 이름과 면적을 인포윈도우에 표시합니다 
    kakao.maps.event.addListener(polygon, 'click', function(mouseEvent) {

        var content ='<div class="info">' + 
                    '   <p class="title">' + area.name + '</p>' +
                    '   <p class="size">총 면적 : 약 ' + Math.floor(polygon.getArea()) + ' m<sup>2</sup></p>' +
                    '   <button type="button" name="chooseArea"> 상권 선택</button>'
                    '</div>';

        infowindow.setContent(content); 
        infowindow.setPosition(mouseEvent.latLng); 
        infowindow.setMap(map);

        // 클릭한 영역 위치로 포커싱
        map.panTo(mouseEvent.latLng); 
```

4. 선택하기 누르면 3가지 데이터가 인풋 값이 입력됨


#### 1) 4개 유형의 상권 영역 좌표 JSON 파일로 저장
> '골목상권, 관광특구, 발달상권, 전통시장' 4개 유형의 상권영역에 대한 정보를 shp(shape)파일로 다운받은 후, 자유 오픈 소스 지리정보 시스템인 'QGIS'을 활용하여 각 상권영역의 꼭짓점 데이터를 위도경도 좌표로 추출하여 JSON 파일로 저장했다.
>> shp 파일의 기존 좌표는 UTMK 투영법과 좌표계를 이용하여 x y 좌표가 '(953937.9, 1952051.9)' 이런 식으로 출력된다. 카카오 지도 API에 사용하기 위해서는 위도 경도 형식으로 바꿔서 '(37.5666805, 126.9784147)'처럼 나타내야 한다. 따라서 QGIS 프로그램 상단에 있는 '플러그인 설치 및 관리'에 들어가서 let latlon tools 플러그인을 설치한다. 그리고 사용할 좌표만 남기고 export하여 JSON 형식의 파일로 다른 이름으로 저장했다.
``` json
[{
	"name": "남영동 먹자골목",
	"LatLng": [
		[37.5405527, 126.9740984],
		[37.540641, 126.9746075],
		[37.5416892, 126.9743639],
		[37.5427344, 126.9740964],
		[37.5437554, 126.9738349],
		[37.5445814, 126.9736291],
		[37.5452626, 126.9734797],
		[37.5452559, 126.9734169],
		[37.545202, 126.9729141],
		[37.5451456, 126.9723904],
		[37.545101, 126.9719936],
		[37.5443504, 126.9721845],
		[37.5435176, 126.9723976],
		[37.5424825, 126.9726592],
		[37.5420662, 126.9727647],
		[37.5414565, 126.9729191],
		[37.54113, 126.9730017],
		[37.540395, 126.9731875],
		[37.5405527, 126.9740984]
	]
}, ...]
```
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

