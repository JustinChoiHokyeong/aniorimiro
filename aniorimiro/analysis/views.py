from django.shortcuts import render
import pandas as pd
import asyncio
from django.http.response import JsonResponse
df=pd.read_csv("https://raw.githubusercontent.com/Kshinhye/aniorimiro_data/master/yongsan_192021.csv", encoding='utf-8')


def map(request):
  analData = df.head(2)

  sub1 = request.GET.get('tradingArea')
  sub2 = request.GET.get('businessType')

  #if request.method == "POST":
    #tradingArea = request.POST.get('tradingArea')
    #businessType = request.POST.get('businessType')
  context = {
    'sub1': sub1,
    'sub2': sub2,
    #'tradingArea':tradingArea,
    #'businessType':businessType
    }
  return render(request, 'analysis/map.html', context)

def calldbFunc(request):
    if request.method=="POST":
        # print('view옴')
        businessType=request.POST.get('businessType')
        # print(businessType)
        tradingArea=request.POST.get('tradingArea')
        # print(tradingArea)
        
        # test="호로로로로롤로로"
        
    return JsonResponse({'tradingArea':tradingArea, 'businessType':businessType})
  
  #if request.method == "POST":
    #tradingArea = request.POST.get('tradingArea')
    #businessType = request.POST.get('businessType')
  # context = {
  #   'sub1': sub1,
  #   'sub2': sub2,
  #   #'tradingArea':tradingArea,
  #   #'businessType':businessType
  #   }
  # # return render(request, 'analysis/map.html', context)


# def ListFunc(request):
#   sum = df
#   context = {'sum': sum}
#   return render(request,'analysis/predict_test.html', context)

# def mapDbFunc(request):
#   if request.method=="GET":
#     id=request.GET['query']
#     data=df[df["상권코드명"]==id]
#     # 이제 원하는대로 데이터를 뽑으면 됩니다. 수업에서 배웠듯이 jikdata생각하시면됩니다.
#     data = {
#       'id' : id,
#       'data' : data
#     }
#   return render(request, 'analysis/map.html', data)

# #1 상권구분 별 점포 수
# def category(SG):
#     GM=pd.DataFrame(df[df['상권구분코드명']==SG])
#     result_SUM=GM["점포수"].sum()
#     return result_SUM

# #2 연령대별 매출 순위
# def nai(NAI):
#     strnai='연령대'+str(NAI)+'매출금액'
#     test3=df.groupby(['서비스업종코드명']).sum()
#     result= test3[strnai].sort_values(ascending=False)
#     return result


  
