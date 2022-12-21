from django.shortcuts import render
import pandas as pd
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

df=pd.read_csv("https://raw.githubusercontent.com/Kshinhye/aniorimiro_data/master/yongsan_192021.csv", encoding='utf-8')


def map(request):
  analData = df.head(2)

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






  
