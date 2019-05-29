from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('poll/<str:slug>/', PollDetail.as_view(), name='poll_detail_url'),
    path('polls', pollsList, name='polls_list_url'),
    path('', mainPage, name='main_page_url'),
]
