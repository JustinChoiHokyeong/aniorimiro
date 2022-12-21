from django.shortcuts import render
import pandas as pd
from django.http import JsonResponse

#데이터 탐색용
df=pd.read_csv("https://raw.githubusercontent.com/Kshinhye/aniorimiro_data/master/yongsan_192021.csv", encoding='utf-8')
#골목상권
df_test1=pd.read_csv("https://raw.githubusercontent.com/JustinChoiHokyeong/BeFourAfterFinal/master/%EC%9A%A9%EC%82%B0%EA%B5%AC_%EA%B3%A8%EB%AA%A9%EC%83%81%EA%B6%8C_%EC%9D%B8%EC%BD%94%EB%94%A9.csv", encoding='utf-8')
#관광특구
df_test2=pd.read_csv("https://raw.githubusercontent.com/JustinChoiHokyeong/BeFourAfterFinal/master/%EC%9A%A9%EC%82%B0%EA%B5%AC_%EA%B4%80%EA%B4%91%ED%8A%B9%EA%B5%AC_%EC%9D%B8%EC%BD%94%EB%94%A9.csv", encoding='utf-8')
#발달상권
df_test3=pd.read_csv("https://raw.githubusercontent.com/JustinChoiHokyeong/BeFourAfterFinal/master/%EC%9A%A9%EC%82%B0%EA%B5%AC_%EB%B0%9C%EB%8B%AC%EC%83%81%EA%B6%8C_%EC%9D%B8%EC%BD%94%EB%94%A9.csv", encoding='utf-8')
#전통시장
df_test4=pd.read_csv("https://raw.githubusercontent.com/JustinChoiHokyeong/BeFourAfterFinal/master/%EC%9A%A9%EC%82%B0%EA%B5%AC_%EC%A0%84%ED%86%B5%EC%8B%9C%EC%9E%A5_%EC%9D%B8%EC%BD%94%EB%94%A9.csv", encoding='utf-8')


def map(request):
  print(df_test1.head(2))
  print(df_test2.head(2))
  print(df_test3.head(2))
  print(df_test4.head(2))

  return render(request, 'analysis/map.html')


def calldbFunc(request):
    if request.method=="POST":
        print('view옴')
        tradingArea=request.POST.get('tradingArea')
        BigTradingArea=request.POST.get('BigTradingArea')
        businessType=request.POST.get('businessType')
        smallBusiType=request.POST.get('smallBusiType')



        context = {
          'businessType':businessType,
          'tradingArea':tradingArea,
          'BigTradingArea':BigTradingArea,
          'smallBusiType':smallBusiType
        }
        
    return JsonResponse(context)






  
