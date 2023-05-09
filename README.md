# 용산구 상권분석 및 매출예측 서비스 프로젝트
* 참여자 : 최호경, 김신혜, 민현진, 윤현성, 정다정, 최현호 (6명)
* 총 개발기간 : 2022/11/26 ~ 2022/12/26 (4주) 

## 목차
* [시연 동영상](#시연-동영상)
* [회의록](#회의록)
* [프로젝트 문서](#프로젝트-문서) 
* [사용 데이터](#사용-데이터)
* [프로젝트 개요](#프로젝트-개요)
* [데이터 분석 과정](#데이터-분석-과정)
* [웹 개발 과정](#웹-개발-과정)
* [미래 개선 방안](#미래-개선-방안)
* [Skills](#skills)
* [참조 사이트](#참조-사이트)

## 시연 동영상
[시연 동영상](https://cliff-celestite-93e.notion.site/33ae79a124b549a584f9c3e2d720adba)

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
* [Figma 사이트맵](https://www.figma.com/file/Alkps3dZyeL7UepkwGyzKG/b4a?node-id=79%3A15)
* 발표 PPT (K-Digital Training 양식)

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
#### 3. 배경
> ‘우리마을가게 상권분석서비스’에 따르면 2022년 2분기 기준 ‘뜨는 동네’ 카테고리에서 이태원상권이 1분기 대비 점포 수, 매출의 증가율이 1위를 하였으며 유동 인구 증가율 또한 4위로 상위권을 차지했다. 이렇듯 이태원을 비롯한 용산구는 주목을 받고 있으며 대통령 집무실 이전으로 인해 관심은 더욱 집중될 것으로 보인다. 그렇지만 ‘뜨는 상권’에서의 용산구는 하위권을 보이고 있다. 
>> 서울시가 제공하는 데이터를 활용하여 용산구의 상권 현황 분석을 실시하고자 한다. 단편적인 정보에 그치지 않고 추가적인 분석을 통해 용산구의 상권 활성화를 위한 인사이트 제시하고자 한다. 또한 용산구의 각 상권의 매출을 포함하여 점포 수, 이용객들의 지표를 살펴보고 매출 예측을 위한 통계학적 모형을 구축하여 예비창업자의 업종선택 및 위치 선정에 도움을 주고, 본 자료를 토대로 용산구의 상권 활성화 방안 모색 탐색에 도움을 주고자 한다.
#### 4. 목적
* 용산구 지역의 예비 창업자와 자영업자에게 운영 및 의사결정에 유용한 상권정보 제공을 통해 용산구 상권 활성화 방안 모색 및 정책 수립 및 집행 과정에 활용
* 탐색적 데이터 분석을 수행하기 위한 데이터 정제, 시각화 방법 학습

## 데이터 분석 과정
------------- 데이터 관련 글 참고해서 쓰기 ------------
### 1. 데이터 탐색 및 전처리
* 변수 정의


#### 1) 데이터 시각화(차트 생성)

```javascript
// 예측 모델 차트 시각화
Highcharts.setOptions({

	lang: {
		thousandsSep: ','
	}
});
Highcharts.chart('container', {
	  chart: {type: 'column'},
	  title: {align: 'center',text: '분기별 예상 매출액'},
	  accessibility: {announceNewData: {enabled: true}},
	  xAxis: {type: 'category'},
	  yAxis: {title: {text: ''}},
	  legend: {enabled: false},
	  plotOptions: {series: {borderWidth: 0,dataLabels: {enabled: true,format: '{point.y:,.0f}원'}}},
	  tooltip: {headerFormat: '<span style="font-size:11px"></span><br>',pointFormat:'<span style="color:{point.color}">{point.name}</span>: {point.y}원<br/>'},
	  series: [{colorByPoint: true,data:
		   [{name: "1분기",y: data.result1,},
		{name: "2분기",y: data.result2,},
		{name: "3분기",y: data.result3,},
		{name: "4분기",y: data.result4,}]}]});
```

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

<img width="418" alt="Screen Shot 2022-12-23 at 5 19 33 PM" src="https://user-images.githubusercontent.com/108642193/209299656-27e222c1-7440-4c88-bc54-8cbc0de6a1db.png">

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
<img width="722" alt="Screen Shot 2022-12-23 at 5 20 56 PM" src="https://user-images.githubusercontent.com/108642193/209299852-c36243af-b817-4871-9ccf-5b69b3b3c71d.png">


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


### 2. 카카오 지도 API 사용
 
> 카카오 지도 API는 지도 상에서 유용하게 사용할 수 있는 다양한 기능을 html+javascript sample 코드로 제공한다. 이를 기반으로 하고, JavaScript와 jQuery를 사용하여 다음과 같은 기능들을 구현했다.

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
} ]
```

#### 2) 상권 영역 독립적으로 출력 및 클릭 가능
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


#### 3) toggle 버튼을 통해 4개 유형 중에 1개씩만 출력
<img width="362" alt="Screen Shot 2022-12-23 at 4 40 53 PM" src="https://user-images.githubusercontent.com/108642193/209293780-f49def5b-6e75-43dc-bd60-5359a7d614a5.png">

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

> if문을 통해 매개변수에 따라 각각 다른 영역이 생성되게 하였고,  버튼이기 때문에 다른 버튼을 또 누르면 기존의 지도는 삭제되게 만들었다. 구체적인 과정은 코드의 주석을 참조.

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



#### 4) 마우스 오버 시, 상권명 표시 및 내부색 활성화
<img width="329" alt="Screen Shot 2022-12-22 at 8 12 51 PM" src="https://user-images.githubusercontent.com/108642193/209122504-9f21a82d-3b0f-4521-960e-ddee0450923e.png">

```javascript 
kakao.maps.event.addListener(polygon, 'mouseover', function(mouseEvent) {
        polygon.setOptions({fillColor: '#09f'});

        customOverlay.setContent('<div class="area">' + area.name + '</div>');
        
        customOverlay.setPosition(mouseEvent.latLng); 
        customOverlay.setMap(map);
    });
```

#### 5) 상권영역 클릭 시 인포윈도우 출력하여 상권명, 영역 넓이 확인 가능 + 클릭 위치를 중심 좌표로 포커싱
<img width="307" alt="Screen Shot 2022-12-23 at 4 42 32 PM" src="https://user-images.githubusercontent.com/108642193/209294047-ccbb35cd-0381-4184-ae3b-520907818910.png">

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

#### 6) 선택하기 누르면 데이터 분석에 필요한 3가지 데이터가 input 태그의 value 값으로 각각 입력됨

> 예측 모델에서 필요한 값이 '대분류 상권', '소분류 상권', '소분류 업종' 3가지 변수이다. 이를 사용자가 선택하여 views.py로 보낼 수 있도록, input 태그의 value로 담기도록 구성하였다.

```javascript 
// 대분류 상권 입력
if(areatype === 'bd'){
    $("#area3").attr("value", "발달상권")
    ...
    }
```

```javascript 
// 소분류 상권 입력
$(document).ready(function(){
      $("button[name='chooseArea']").click(function(){
      $("#area1").text(area.name);
      $("#area2").attr("value", area.name)
    })
  }) 
```

<img width="518" alt="Screen Shot 2022-12-23 at 4 51 18 PM" src="https://user-images.githubusercontent.com/108642193/209295502-84922297-fb8f-4355-87ec-f19dae760a52.png">


<img width="367" alt="Screen Shot 2022-12-23 at 4 45 15 PM" src="https://user-images.githubusercontent.com/108642193/209294497-e49ceaa5-9d10-474a-8ee3-e08488b0e849.png">

> 대분류 업종을 선택하면 서로 다르게 해당되는 소분류 업종 리스트가 출력되도록 구성함.

```javascript 
// 소분류 업종
function selectBusi(){
        var bigBusi = document.querySelector("#selectBusiType")
        var smallBusi = document.querySelector("#smallCategory")
        var bigOption = bigBusi.options[bigBusi.selectedIndex].innerText;

        var subOptions = {
        food:['분식전문점', '양식음식점', '일식음식점', '제과점', '중식음식점', '치킨전문점', '커피-음료', '패스트푸드점', '한식음식점', '호프-간이주점'],
        service:['PC방', '가전제품수리', '고시원', '골프연습장', '네일숍', '노래방', '당구장', '미용실', '부동산중개업', '세탁소', '스포츠 강습', '스포츠클럽', '여관', '예술학원', '외국어학원', '일반교습학원', '일반의원', '자동차미용', '자동차수리', '치과의원', '피부관리실', '한의원'],
        retail:['가구', '가방', '가전제품', '문구', '미곡판매', '반찬가게', '서적', '섬유제품', '수산물판매', '슈퍼마켓', '시계및귀금속', '신발', '안경', '애완동물', '완구', '운동/경기용품', '육류판매', '의료기기', '의약품', '인테리어', '일반의류', '자전거 및 기타운송장비', '전자상거래업', '조명용품', '철물점', '청과상', '컴퓨터및주변장치판매', '편의점', '핸드폰', '화장품', '화초']
        }

        switch(bigOption){
          case "외식업":
            var subOption = subOptions.food;
            break;
          case "서비스업":
            var subOption = subOptions.service;
            break;
          case "소매업":
            var subOption = subOptions.retail;
            break;
        }

        smallBusi.options.length = 0;

        for(var i=0; i < subOption.length; i++){
          var option = document.createElement('option');
          option.innerText = subOption[i];
          option.value = subOption[i];
          smallBusi.append(option);
        }
      }

```

<img width="362" alt="Screen Shot 2022-12-23 at 4 46 15 PM" src="https://user-images.githubusercontent.com/108642193/209294680-b378e8cd-4473-46cd-8eb7-071bfb4d4ef2.png">

> form 안에 input의 value로 views.py 로 넘겨줄 값들이 담긴 것을 확인할 수 있음.

```javascript 
<form method="post" id="sform">{% csrf_token %}
      <!-- <label for="tradingarea" >대분류 상권:</label> -->
      <input type="hidden" id=area3 value="" name="BigTradingArea"><br/>
      <label for="tradingarea" >상권 이름:</label><br />
      <!-- <span id=area1> </span><br/> -->
      <input type="text" id=area2 value="" name="tradingArea"><br/>
      <label for="tradingarea" >대분류 업종:</label>
      <ul>
	      <select name="businessType" id="selectBusiType" onchange="selectBusi()" class="sele">
	        <option value="" selected disabled>업종을 선택해주세요</option>
	        <option value="외식업" >외식업</option>
	        <option value="서비스업">서비스업</option>
	        <option value="소매업">소매업</option>
	      </select>
	  </ul>  
	  <br/>
      <label for="tradingarea" >소분류 업종:</label>
      <ul>
	      <select name="smallBusiType" id="smallCategory">
	      </select>
	  </ul>
      <br />
      <hr />
      <!-- form 에서 onclick 속성을 사용 시 새로고침을 피할 수 없다.-->
      <!-- 1. button -> div/span 로 바꾼다. 2. button 태그를 줬다면 type="button"속성을 추가해준다 -->
      <button onclick="ajaxSend()" type="button" id="reportBtn">분석하기</button>
</form>
```

### 3. JQuery Ajax 데이터 전달

<img width="348" alt="Screen Shot 2022-12-23 at 4 47 06 PM" src="https://user-images.githubusercontent.com/108642193/209294819-f7eadfaa-abdd-4796-97fc-3c208e39aaaf.png">

> input 태그에 value를 담은 뒤 '분석하기' 클릭하면, 제이쿼리의 ajax 기능을 통해서 views.py로 데이터를 넘겨줌.

```javascript 
function ajaxSend(){
        //alert("제출클릭됨!!")
        let data = $("#sform").serialize();
        return $.ajax({
            url:"/analysis/calldb/",
            type:"post",
            data:data,
            dataType:"json",
            success:function(data){
            //innerText보다 textContent가 속도가 빠르다
            //상권 소분류(1~40)
            document.querySelector("#showData2").textContent =data.tradingArea;
            //상권 대분류(1~4)
            document.querySelector("#showData3").textContent =data.BigTradingArea;

            //소분류 업종(1~30)
            document.querySelector("#showData4").textContent =data.smallBusiType;
            //대분류 업종(고유 코드 필요X, 사용자 확인용)
            document.querySelector("#showData1").textContent =data.businessType;
	    ...
	    }
```

> input의 value에 입력된 값을 json 타입으로 보내기 위해 serialize해주고, analysis 앱의 views.py에 있는 calldb 함수로 data를 전송한다. views에서는 input 요소의 name을 가지고 각 데이터를 받아와서 사용한다. 받아온 데이터는 함수 내부에서 예측 모델로 처리하거나 사용자에게 출력해줄 변수를 정리해서 context에 key:value 형태로 담아서 다시 html 파일로 보내준다. 받아온 데이터는 특정 id 값을 가진 요소의 textContent로 입력해주면, 사용자가 볼 수 있는 화면에 잘 출력되는 것을 확인할 수 있다.

```python
#views.py
def calldbFunc(request):
    
    if request.method=="POST":
        print('view옴')
        tradingArea=request.POST.get('tradingArea')
        BigTradingArea=request.POST.get('BigTradingArea')
        businessType=request.POST.get('businessType')
        smallBusiType=request.POST.get('smallBusiType')
	
	...
	
	context = {
	  'businessType':businessType,
	  'tradingArea':tradingArea,
	  'BigTradingArea':BigTradingArea,
	  'smallBusiType':smallBusiType,
	  'result1':result1,
	  'result2':result2,
	  'result3':result3,
	  'result4':result4
	}

    return JsonResponse(context)
```

<img width="511" alt="Screen Shot 2022-12-23 at 4 49 19 PM" src="https://user-images.githubusercontent.com/108642193/209295160-db113395-497a-4854-a5cf-f131ce1bbcee.png">




### 4. CSS

#### 1) Figma를 사용해서 웹 디자인 및 사이트맵 구성
<img width="448" alt="Screen Shot 2022-12-23 at 11 15 53 AM" src="https://user-images.githubusercontent.com/108642193/209257579-3edf3c35-9bfb-4f2e-8cbe-763ae8e7fe60.png">

> 피그마 툴을 사용하여 전체 웹 및 구성요소들을 디자인하고, 이를 기반으로 css를 작성하였다. 

#### 2) 외부 CSS 파일 정리

> 각각의 html tag, class, id에 해당하는 디자인 속성을 외부 css 파일로 분리하여, 한 곳에 모아서 작성하여 유지보수성을 높였다. css 학습을 위해 부트스트랩 같은 라이브러리를 사용하지 않고, 웹 브라우저의 검사 기능을 사용하여 비교하면서 세부적인 요소들을 코딩하였다. 이를 통해 다양한 toggle 기능, 애니메이션 효과 등을 구현할 수 있었다.

```css
/* 3. 상권 분석, 매출 예측 */

html, body {width:100%;height:100%;margin:0;padding:0;overflow: auto;} 

/* 3-1. 상권 분석 map */
.areacontrol {font-size:12px;position:fixed;top:58px;left:10px;height:30px;margin:0;padding:0;z-index:1;font-family:'Malgun Gothic', '맑은 고딕', 'sans-serif';}
.areacontrol .radius_border{border:1px solid #919191;border-radius:5px;}
.areacontrol span {display:block;width:84px;height:50px;float:left;text-align:center;line-height:50px;cursor:pointer;border: 2px ridge;}

.areacontrol .btn {padding:0;font-size:15px;line-height:50px;background:linear-gradient(#e8e8e8,  #fff);border-radius: 10px;}
.areacontrol .btn:hover {background:#f5f5f5;background:linear-gradient(#f5f5f5,#e3e3e3);border-color:#E9AA13; color:#E9AA13;}
.areacontrol .btn:active {background:#e6e6e6;background:linear-gradient(#e6e6e6, #fff);border-color:#F9AB00; color:#591035;}
.areacontrol .selected_btn {color:#591035;background:linear-gradient(#fff7dc, #ffd442);font-size: 15px;border-radius: 10px;}/*background:linear-gradient(#425470, #5b6d8a);*/
.areacontrol .selected_btn:hover {color:#591035;}

/* 3-1-1. 좌측 상단 카테고리 선택 (상권 & 업종) */
.leftCategory {position:absolute;top:115px;left:10px;width:315px; height:400px;margin:0;padding:0 20px; z-index:1;background-color:#fff;border-radius: 10px;}
.leftCategory > h3 {font-size:24px;text-align: left;color: #0676DD; padding:15px 0;}
.leftCategory > hr {border-right-width: 0px;border-top-width: 0px;border-bottom-width: 2px;border-left-width: 0px;margin-bottom: 10px;}
.leftCategory > form > ul > select{appearance:none;border-radius: 5px; width: 100% !important; height:36px;padding: 0 40px 0 20px; padding-top:2px; margin-top:5px; border: 1px solid #999;font-size: 14px;line-height: 34px; background:url(/static/pictures/arrow_bottom.svg) no-repeat right 20px center/10px auto #fff;}
.leftCategory > form > input{height: 20px; padding: 5px 0;margin-top: 10px;margin-bottom:10px;padding-left: 10px;width: 205px;}
.leftCategory > form > button{padding: 10px 50px;margin-top: 15px;margin-left: 70px;border: 2px ridge;background:linear-gradient(#e8e8e8,  #fff);border-radius: 10px;}
.leftCategory > form > button:hover {background:#f5f5f5;background:linear-gradient(#f5f5f5,#e3e3e3);border-color:rgb(11, 103, 217); color:#0676dd;}
.leftCategory > form > button:active {background:#e6e6e6;background:linear-gradient(#e6e6e6, #fff);border-color:#0B7FD3; color:#0676dd;}
.leftCategory > form > hr {border-right-width: 0px;border-top-width: 0px;border-bottom-width: 2px;border-left-width: 0px;margin-bottom: 10px;}
```


#### 3) 로그인, 회원가입 폼 css 입력 - 장고 템플릿 오류 해결
> 장고에서 제공하는 로그인, 회원가입 form을 사용하였기 때문에, 템플릿 태그를 사용하여 html 파일에서 입력창을 형성한다. 

```html
<div class="signin-container">
        <div class="account-box" type="text">{{ form.username }}</div>
</div>
```

<img width="406" alt="Screen Shot 2022-12-23 at 12 20 47 PM" src="https://user-images.githubusercontent.com/108642193/209264500-479d3b9f-6839-4b4f-a1e1-47d615266f9f.png">

> 웹 브라우저 검사를 통해서 보면, {{ form.username }} 이 템플릿 태그 자체가 input 태그로 변형되어 출력됨을 확인할 수 있다. 따라서 css를 입력할 때, class 내부의 input 요소로 디자인 속성을 걸어서 입력해야 한다.


## 미래 개선 방안

### 1. 데이터 분석
[데이터 분석 보고서](https://cliff-celestite-93e.notion.site/33ae79a124b549a584f9c3e2d720adba)

### 2. 웹 개발
#### 1) 마이페이지 스크랩 저장 기능
> 출력된 분석 결과 보고서를 이미지로 DB에 저장하고 마이페이지에서 게시판 형태로 조회 및 관리가 가능하도록 구성한다. 그러면 로그인 기능과 조합하여 활용할 수 있을 것으로 기대한다.
#### 2) 인포윈도우 -> 커스텀 오버레이로 수정
> 카카오 지도 API에서 제공하는 윈포윈도우 기능은 사용자에 의해 수정이 불가하다. 따라서 커스텀 오버레이로 대체시키면 다양한 형태로 재구성시켜서 더 많은 정보를 담을 수 있고 동시에 사용자 경험도 높일 수 있을 것으로 기대한다.
#### [3) AWS 클라우드 서버 출력](https://justdojustin.tistory.com/58)
> AWS EC2 를 활용하여 원격 IP로 언제 어느 컴퓨터에서도 웹 사이트에 접속가능하도록 시도했던 경험이 있다. ssh 명령어를 통해 클라우드 서버에 있는 아파치를 통해서 우븐투 리눅스 환경에 접속하였고, 제작 중이었던 장고 프로젝트를 실행시켜 보았다. 하지만 가용한 리소스가 충분하지 않아서 페이지 로딩이 너무 느려지는 이슈를 만나게 되었다. 따라서 현재는 로컬에서 장고 서버를 통해 웹 사이트를 출력하고 있으며, 프로젝트 완성 후 다시 클라우드 서버를 통한 출력을 시도해볼 계획이다.






## Skills
* **OS** : Windows, MacOS
* **Language** : Python, HTML5, CSS3, JavaScript(ES6)
* **Framework/Library** : Django, Numpy, Pandas, SciPy, Statsmodels, Highcharts, Chart.js, jQurey
* **Database** : MariaDB
* **IDE** : Eclipse, VS Code
* **Collaboration** : GitHub, Slack, Discord, Google Sheets, Figma

## 참조 사이트
1. [우리마을가게 상권분석서비스](https://golmok.seoul.go.kr/main.do)
2. [소상공인마당 상권정보](https://sg.sbiz.or.kr/godo/index.sg)
3. [카카오 지도 API](https://apis.map.kakao.com/web/)
4. [shp 파일 영역좌표 추출 사이트(QGIS)](https://www.qgis.org/ko/site/)
5. [JSON 파일 유효성 검증 사이트](https://jsonlint.com/)

