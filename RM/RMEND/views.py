from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'RMEND/index.html')

def about(request):
    return render(request,'RMEND/about.html')
def news_1(request):
    return  render(request,'RMEND/news-1.html')
def news_2(request):
    return  render(request,'RMEND/news-2.html')
def news_3(request):
    return  render(request,'RMEND/news-3.html')
def news_4(request):
    return  render(request,'RMEND/news-4.html')
