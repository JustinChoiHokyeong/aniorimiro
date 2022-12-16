from django.shortcuts import render
import pandas as pd

df=pd.read_csv("https://raw.githubusercontent.com/Kshinhye/aniorimiro_data/master/yongsan_192021.csv", encoding='utf-8')

def map(request):

  return render(request, 'analysis/map.html')



def ListFunc(request):
  sum = df
  context = {'sum': sum}
  return render(request,'analysis/predict.html', context)
# 함수



#1 상권구분 별 점포 수
def category(SG):
    GM=pd.DataFrame(df[df['상권구분코드명']==SG])
    result_SUM=GM["점포수"].sum()
    return result_SUM

#2 연령대별 매출 순위
def nai(NAI):
    strnai='연령대'+str(NAI)+'매출금액'
    test3=df.groupby(['서비스업종코드명']).sum()
    result= test3[strnai].sort_values(ascending=False)
    return result

#3 상권별(서비스 업종) 점포수 ( 분기별 대비 )
# CS100001 ~ CS100010 #외식업 WS
# CS200001 ~ CS200037 #서비스업 SBS
# CS300001 ~ CS300043 #소매업 SM

#4 인기 업종 ( 분기별 증감률 )

##매출 분석
#5 점포별 월평균 매출액 (분기별 증감률 : 전국, 서울과 비교)
#6 점포별 월평균 매출 건수 (분기별 증감률 : 전국, 서울과 비교)
#7 요일별 매출분석 ( 할 수 있다면 서울시와 비교)
#8 시간대별
#9 성별별 ( + 각 업종마다 성별의 매출비교 )
#10 연령대별 각업종 매출비율