from django.shortcuts import render
import json

def map(request):

  return render(request, 'analysis/map.html')

