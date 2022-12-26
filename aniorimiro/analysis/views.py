# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings(action='ignore')# 경고출력안하기
import scipy.stats as stats
# from sklearn.preprocessing import LabelEncoder   
import statsmodels.formula.api as smf

pd.options.display.float_format = '{:.5f}'.format
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

from django.shortcuts import render
from django.http import JsonResponse

def map(request):
  return render(request, 'analysis/map.html')

def calldbFunc(request):
    # map.html 에서 post방식으로 form 이 넘어온다.
    if request.method=="POST":
        print('view옴')
        # 상권구분코드명(골목상권, 발달상권, 전통시장, 관광특구)
        BigTradingArea=request.POST.get('BigTradingArea')
        # 상권코드명
        tradingArea=request.POST.get('tradingArea')
        # 서비스업종 대분류
        businessType=request.POST.get('businessType')
        # 서비스업종 소분류
        smallBusiType=request.POST.get('smallBusiType')
        
        print('BigTradingArea:',BigTradingArea)
        print('tradingArea:',tradingArea)
        print('smallBusiType',smallBusiType)

        ###################   예측 predict data   ###################
        # tradingArea,smallBusiType를 받는 predict 함수 호출
        # 상권마다 모델이 다르다. 해당 상권에 변수에 맞춰 새로운 예측변수를 가져온다.
        mdata=pd.read_csv("https://raw.githubusercontent.com/Kshinhye/aniorimiroDATA/master/yongsan2021.csv")

        if BigTradingArea == "골목상권":
            pdata=golpredx(tradingArea,smallBusiType) 
            gol= mdata[mdata['상권_구분_코드_명']=='골목상권']
            lm=smf.ols(formula='분기당_매출_금액 ~ 월요일_매출_금액 + 금요일_매출_금액 + 남성_매출_금액 + 수요일_매출_금액 + 화요일_매출_금액', data=gol).fit()
            
        elif BigTradingArea == "발달상권":
            pdata=balpredx(tradingArea,smallBusiType)
            bal= mdata[mdata['상권_구분_코드_명']=='발달상권']
            lm=smf.ols(formula='분기당_매출_금액 ~ 시간대_14_17_매출_금액 + 수요일_매출_금액 + 시간대_11_14_매출_금액 + 월요일_매출_금액 + 금요일_매출_금액', data=bal).fit()
            
        elif BigTradingArea == "전통시장":
            pdata=jpredx(tradingArea,smallBusiType) 
            jeon= mdata[mdata['상권_구분_코드_명']=='전통시장']
            lm=smf.ols(formula='분기당_매출_금액 ~ 금요일_매출_금액 + 수요일_매출_금액 + 여성_매출_금액 + 화요일_매출_금액 + 목요일_매출_금액', data=jeon).fit()
            
        elif BigTradingArea == "관광특구":
            pdata=culpredx(tradingArea,smallBusiType)
            cul= mdata[mdata['상권_구분_코드_명']=='관광특구']
            lm=smf.ols(formula='분기당_매출_금액 ~ 남성_매출_금액 + 연령대_40_매출_금액 + 시간대_14_17_매출_금액 + 화요일_매출_금액 + 시간대_17_21_매출_금액', data=cul).fit()
            
        print('pdata :',pdata)
               
        # 해당 상권에 선택한 서비스업종이 있다면
        if not pdata.empty :
            if '1분기' in pdata.index:
                pred1 = lm.predict(pdata.loc['1분기'])
            else : pred1 = pd.DataFrame({'A' : [np.nan]})
            if '2분기' in pdata.index:
                pred2 = lm.predict(pdata.loc['2분기'])
            else : pred2 = pd.DataFrame({'A' : [np.nan]})
            if '3분기' in pdata.index:
                pred3 = lm.predict(pdata.loc['3분기'])
            else : pred3 = pd.DataFrame({'A' : [np.nan]})
            if '4분기' in pdata.index:
                pred4 = lm.predict(pdata.loc['4분기'])
            else : pred4 = pd.DataFrame({'A' : [np.nan]})
            print(pred1, type(pred1))
            print(pred2)
            print(pred3)
            print(pred4)
            # predict 값에서 values로 꺼내면 ndarray로 담기는데, json으로 넘길 수 없어서 list로 바꿔준다
            if pred1.dropna().empty == False:
                result1 = round((pred1/ pdata['점포수'].iloc[0]).values.tolist()[0])
            else : result1 =0
            
            if pred2.dropna().empty == False:
                result2 = round((pred2/ pdata['점포수'].iloc[1]).values.tolist()[0])
            else : result2 =0    
            
            if pred3.dropna().empty == False:
                result3 = round((pred3/ pdata['점포수'].iloc[2]).values.tolist()[0])
            else : result3 =0    
            
            if pred4.dropna().empty == False:
                result4 = round((pred4/ pdata['점포수'].iloc[3]).values.tolist()[0])
            else : result4 =0
            
            ################### 분석 report data   ###################
            # tradingArea,smallBusiType를 받는 report함수 호출
            rdata=report(BigTradingArea,tradingArea,smallBusiType)
            print('rdata :',rdata)
            # index=1,2,3,4분기 columns=2019, 2020, 2021년
            jum19= rdata[0]['2019'].values.tolist()
            jum20= rdata[0]['2020'].values.tolist()
            jum21= rdata[0]['2021'].values.tolist()
            # index=남,녀 columns=2019, 2020, 2021년
            gen19= rdata[1]['2019'].values.tolist()
            print(rdata[1]['2019'])
            gen20= rdata[1]['2020'].values.tolist()
            gen21= rdata[1]['2021'].values.tolist()
            # index='00_06','06_11','11_14','14_17','17_21','21_24' columns=2019, 2020, 2021년
            time19= rdata[2]['2019'].values.tolist()
            time20= rdata[2]['2020'].values.tolist()
            time21= rdata[2]['2021'].values.tolist()
        # 0이 넘어온다면 0을 담는다.
        else:
            result1=0; result2=0; result3=0; result4=0; jum19=0; jum20=0; jum21=0; 
            gen19=0; gen20=0; gen21=0; time19=0; time20=0; time21=0; 
            
            
        preData={
            'businessType':businessType,
            'tradingArea':tradingArea,
            'BigTradingArea':BigTradingArea,
            'smallBusiType':smallBusiType,
            
            'result1':result1,
            'result2':result2,
            'result3':result3,
            'result4':result4           
        }
        
        reportData={
            'jum19':jum19,
            'jum20':jum20,
            'jum21':jum21,
            
            'gen19':gen19,
            'gen20':gen20,
            'gen21':gen21,
            
            'time19':time19,
            'time20':time20,
            'time21':time21
        }
        
    return JsonResponse({'preData':preData,'reportData':reportData})

dfdata=pd.read_csv("https://raw.githubusercontent.com/Kshinhye/aniorimiroDATA/master/yongsan2021.csv", encoding='utf-8')
def report(BigTradingArea,tradingArea,smallBusiType):
    global dfdata
    df=dfdata[dfdata['상권_구분_코드_명']==BigTradingArea]
    sang = df[df['상권_코드_명']==tradingArea]
    # 선택한 업종이 있으면 데이터를 불러오고 없으면 0을 리턴한다.
    if smallBusiType in list(sang['서비스_업종_코드_명']):
        # 선택한 서비스업종의 행들만 불러온다.
        service = sang[sang['서비스_업종_코드_명']==smallBusiType]  
                   
        ###### 분석 리포트에 출력 할 자료이다.
        # 년도별로 나타낼 예정이라 년도별로 담아준다.   
        s19=service[service['기준_년_코드']==2019]
        s20=service[service['기준_년_코드']==2020]
        s21=service[service['기준_년_코드']==2021]
        
        # 해당년도의 점포수를 가져와
        jum19=[]
        jum20=[]
        jum21=[]
        # 19년도
        if 1 in s19['기준_분기_코드'].values:
            jum19.append(s19[s19['기준_분기_코드']==1]['점포수'].values[0])
        else : jum19.append(0)
        
        if 2 in s19['기준_분기_코드'].values:
            jum19.append(s19[s19['기준_분기_코드']==2]['점포수'].values[0])
        else : jum19.append(0)
        
        if 3 in s19['기준_분기_코드'].values:
            jum19.append(s19[s19['기준_분기_코드']==3]['점포수'].values[0])
        else : jum19.append(0)
        
        if 4 in s19['기준_분기_코드'].values:
            jum19.append(s19[s19['기준_분기_코드']==4]['점포수'].values[0])
        else : jum19.append(0)
        
        # 20년도
        if 1 in s20['기준_분기_코드'].values:
            jum20.append(s20[s20['기준_분기_코드']==1]['점포수'].values[0])
        else : jum20.append(0)
        
        if 2 in s20['기준_분기_코드'].values:
            jum20.append(s20[s20['기준_분기_코드']==2]['점포수'].values[0])
        else : jum20.append(0)
        
        if 3 in s20['기준_분기_코드'].values:
            jum20.append(s20[s20['기준_분기_코드']==3]['점포수'].values[0])
        else : jum20.append(0)
        
        if 4 in s20['기준_분기_코드'].values:
            jum20.append(s20[s20['기준_분기_코드']==4]['점포수'].values[0])
        else : jum20.append(0)
        
        # 21년도
        if 1 in s21['기준_분기_코드'].values:
            jum21.append(s21[s21['기준_분기_코드']==1]['점포수'].values[0])
        else : jum21.append(0)
        
        if 2 in s21['기준_분기_코드'].values:
            jum21.append(s21[s21['기준_분기_코드']==2]['점포수'].values[0])
        else : jum21.append(0)
        
        if 3 in s21['기준_분기_코드'].values:
            jum21.append(s21[s21['기준_분기_코드']==3]['점포수'].values[0])
        else : jum21.append(0)
        
        if 4 in s21['기준_분기_코드'].values:
            jum21.append(s21[s21['기준_분기_코드']==4]['점포수'].values[0])
        else : jum21.append(0)
        
        # dataframe에 담아준다.
        jum=pd.DataFrame(zip(jum19,jum20,jum21), columns=['2019','2020','2021'], index=['1분기','2분기','3분기','4분기'])
        
        # 해당년도의 남.녀 매출 비율의 가져와
        if len(s19) != 0:
            jen19 = s19[['남성_매출_비율','여성_매출_비율']].iloc[0].values
            print(jen19,type(jen19))
        else : jen19 = np.array([0,0])
        if len(s20) != 0:
            jen20 = s20[['남성_매출_비율','여성_매출_비율']].iloc[0].values
        else : jen20 = np.array([0,0])
        if len(s21) != 0:
            jen21 = s21[['남성_매출_비율','여성_매출_비율']].iloc[0].values
        else : jen21 = np.array([0,0])    
        # dataframe에 담아준다.
        jen=pd.DataFrame(zip(jen19,jen20,jen21), columns=['2019','2020','2021'], index=['남','여'])
        # 해당년도의 시간대 매출 비율의 가져와
        if len(s19) != 0:
            time19 = s19[['시간대_00_06_매출_비율','시간대_06_11_매출_비율','시간대_11_14_매출_비율','시간대_14_17_매출_비율','시간대_17_21_매출_비율','시간대_21_24_매출_비율']].iloc[0].values
        else : time19 = np.array([0,0,0,0,0,0])
        if len(s20) != 0:
            time20 = s20[['시간대_00_06_매출_비율','시간대_06_11_매출_비율','시간대_11_14_매출_비율','시간대_14_17_매출_비율','시간대_17_21_매출_비율','시간대_21_24_매출_비율']].iloc[0].values
        else : time20 = np.array([0,0,0,0,0,0])
        if len(s21) != 0:
            time21 = s21[['시간대_00_06_매출_비율','시간대_06_11_매출_비율','시간대_11_14_매출_비율','시간대_14_17_매출_비율','시간대_17_21_매출_비율','시간대_21_24_매출_비율']].iloc[0].values
        else : time21 = np.array([0,0,0,0,0,0])
        # dataframe에 담아준다.
        time=pd.DataFrame(zip(time19,time20,time21), columns=['2019','2020','2021'], index=['00_06','06_11','11_14','14_17','17_21','21_24'])

        return jum, jen, time
 
def balpredx(tradingArea,smallBusiType):
    global dfdata
    df=dfdata[dfdata['상권_구분_코드_명']=="발달상권"]
    sang = df[df['상권_코드_명']==tradingArea]
    # 선택한 업종이 있으면 데이터를 불러오고 없으면 0을 리턴한다.
    if smallBusiType in list(sang['서비스_업종_코드_명']):
        # 선택한 서비스업종의 행들만 불러온다.
        service = sang[sang['서비스_업종_코드_명']==smallBusiType]
        
        ###### 모델에 넣어줄 미지의 값이다.(예측값에 사용)
        # 분기별 평균을 구한다.
        xdata=service.groupby(service['기준_분기_코드']).mean()
        # 예측값에 넣을 변수들만 담기위해 빈 데이터 프레임을 만들어준다.
        predictdata=pd.DataFrame()
        # 산정이 안된 분기가 있을 경우 길이를 모르기때문에 index를 돈다.
        for i in xdata.index:
            # 0부터 시작하기때문에 -1을 해준다.
            df = pd.DataFrame({'시간대_14_17_매출_금액':xdata['시간대_14_17_매출_금액'].iloc[i-1],
                              '수요일_매출_금액':xdata['수요일_매출_금액'].iloc[i-1],
                              '시간대_11_14_매출_금액':xdata['시간대_11_14_매출_금액'].iloc[i-1],
                              '월요일_매출_금액':xdata['월요일_매출_금액'].iloc[i-1],
                              '금요일_매출_금액':xdata['금요일_매출_금액'].iloc[i-1],
                              '점포수':xdata['점포수'].iloc[i-1]})
            
            # 위 행들을 준비해둔 데이터 프레임에 담아준다.
            predictdata=pd.concat([predictdata,df])
            # 계속돈다.
            i+1
        return predictdata
    else:
        return pd.DataFrame()
    
def golpredx(tradingArea,smallBusiType):
    global dfdata
    df=dfdata[dfdata['상권_구분_코드_명']=="골목상권"]
    sang = df[df['상권_코드_명']==tradingArea]
    # 선택한 업종이 있으면 데이터를 불러오고 없으면 0을 리턴한다.
    if smallBusiType in list(sang['서비스_업종_코드_명']):
        # 선택한 서비스업종의 행들만 불러온다.
        service = sang[sang['서비스_업종_코드_명']==smallBusiType]
        
        ###### 모델에 넣어줄 미지의 값이다.(예측값에 사용)
        # 분기별 평균을 구한다.
        xdata=service.groupby(service['기준_분기_코드']).mean()
        # 예측값에 넣을 변수들만 담기위해 빈 데이터 프레임을 만들어준다.
        predictdata=pd.DataFrame()
        # 산정이 안된 분기가 있을 경우 길이를 모르기때문에 index를 돈다.
        print(xdata)
        for i in xdata.index:
            print(i)
            # 0부터 시작하기때문에 -1을 해준다.
            df = pd.DataFrame({'월요일_매출_금액':xdata['월요일_매출_금액'].iloc[i-1],
                              '금요일_매출_금액':xdata['금요일_매출_금액'].iloc[i-1],
                              '남성_매출_금액':xdata['남성_매출_금액'].iloc[i-1],
                              '수요일_매출_금액':xdata['수요일_매출_금액'].iloc[i-1],
                              '화요일_매출_금액':xdata['화요일_매출_금액'].iloc[i-1],
                              '점포수':xdata['점포수'].iloc[i-1]},index = [str(i)+'분기'])
            
            # 위 행들을 준비해둔 데이터 프레임에 담아준다.
            predictdata=pd.concat([predictdata,df])
            # 계속돈다.
            i+1
        return predictdata 
    else:
        return pd.DataFrame()

def jpredx(tradingArea,smallBusiType):
    global dfdata
    df=dfdata[dfdata['상권_구분_코드_명']=="전통시장"]
    sang = df[df['상권_코드_명']==tradingArea]
    # 선택한 업종이 있으면 데이터를 불러오고 없으면 0을 리턴한다.
    if smallBusiType in list(sang['서비스_업종_코드_명']):
        # 선택한 서비스업종의 행들만 불러온다.
        service = sang[sang['서비스_업종_코드_명']==smallBusiType]
        
        ###### 모델에 넣어줄 미지의 값이다.(예측값에 사용)
        # 분기별 평균을 구한다.
        xdata=service.groupby(service['기준_분기_코드']).mean()
        # 예측값에 넣을 변수들만 담기위해 빈 데이터 프레임을 만들어준다.
        predictdata=pd.DataFrame()
        # 산정이 안된 분기가 있을 경우 길이를 모르기때문에 index를 돈다.
        for i in xdata.index:
            # 0부터 시작하기때문에 -1을 해준다.
            df = pd.DataFrame({'금요일_매출_금액':xdata['금요일_매출_금액'].iloc[i-1],
                              '수요일_매출_금액':xdata['수요일_매출_금액'].iloc[i-1],
                              '여성_매출_금액':xdata['여성_매출_금액'].iloc[i-1],
                              '화요일_매출_금액':xdata['화요일_매출_금액'].iloc[i-1],
                              '목요일_매출_금액':xdata['목요일_매출_금액'].iloc[i-1],
                              '점포수':xdata['점포수'].iloc[i-1]},index = [str(i)+'분기'])
            
            # 위 행들을 준비해둔 데이터 프레임에 담아준다.
            predictdata=pd.concat([predictdata,df])
            # 계속돈다.
            i+1

        return predictdata
    else:
        return pd.DataFrame()

def culpredx(tradingArea,smallBusiType):
    global dfdata
    print("관광")
    df=dfdata[dfdata['상권_구분_코드_명']=="관광특구"] 
    sang = df[df['상권_코드_명']==tradingArea]
    print(sang)
    # 선택한 업종이 있으면 데이터를 불러오고 없으면 0을 리턴한다.
    if smallBusiType in list(sang['서비스_업종_코드_명']):
        # 선택한 서비스업종의 행들만 불러온다.
        service = sang[sang['서비스_업종_코드_명']==smallBusiType]
        
        ###### 모델에 넣어줄 미지의 값이다.(예측값에 사용)
        # 분기별 평균을 구한다.
        xdata=service.groupby(service['기준_분기_코드']).mean()
        # 예측값에 넣을 변수들만 담기위해 빈 데이터 프레임을 만들어준다.
        predictdata=pd.DataFrame()
        # 산정이 안된 분기가 있을 경우 길이를 모르기때문에 index를 돈다.
        for i in xdata.index:
            print(i)
            # 0부터 시작하기때문에 -1을 해준다.
            df = pd.DataFrame({'남성_매출_금액':xdata['남성_매출_금액'].iloc[i-1],
                              '연령대_40_매출_금액':xdata['연령대_40_매출_금액'].iloc[i-1],
                              '시간대_14_17_매출_금액':xdata['시간대_14_17_매출_금액'].iloc[i-1],
                              '화요일_매출_금액':xdata['화요일_매출_금액'].iloc[i-1],
                              '시간대_17_21_매출_금액':xdata['시간대_17_21_매출_금액'].iloc[i-1],
                              '점포수':xdata['점포수'].iloc[i-1]},index = [str(i)+'분기'])
            
            # 위 행들을 준비해둔 데이터 프레임에 담아준다.
            predictdata=pd.concat([predictdata,df])
            # 계속돈다.
            i+1
        return predictdata 
    else:
        return pd.DataFrame()