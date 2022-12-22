from django.shortcuts import render
import pandas as pd
from django.http import JsonResponse

df=pd.read_csv("https://raw.githubusercontent.com/Kshinhye/aniorimiro_data/master/yongsan_192021.csv", encoding='utf-8')


def map(request):
  analData = df.head(2)

  return render(request, 'analysis/map.html')


def calldbFunc(request):
    if request.method=="POST":
        print('view옴')
        trading=request.POST.get('tradingArea')
        BigTrading=request.POST.get('BigTradingArea')
        business=request.POST.get('businessType')
        smallBusi=request.POST.get('smallBusiType')
        context = {
          'trading':trading,
          'BigTrading':BigTrading,
          'business':business,
          'smallBusi':smallBusi
        }
        
    return JsonResponse(context)
