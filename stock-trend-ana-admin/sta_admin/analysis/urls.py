__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '2/4/2021 11:01 AM'

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('error/', views.bad_request, name='diff_name'),
    path('news/latest/<str:stock>', views.get_latest_news, name="get_news")
]