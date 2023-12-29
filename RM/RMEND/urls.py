from django.urls import path
from .views import *

urlpatterns = [
    path('',index, name='home'),
    path('about/',about, name='history'),
    path('news-1/',news_1,name='RealMadrid|news|MaryChristmast'),
    path('news-2/', news_2, name='RealMadrid|news|training'),
    path('news-3/', news_3, name='RealMadrid|news|transfer'),
    path('news-4/', news_4, name='RealMadrid|news|bestDefender')
]