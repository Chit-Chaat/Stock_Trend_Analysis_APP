__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '2/4/2021 11:01 AM'

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('test/', views.test, name='index'),
    path('error/', views.bad_request, name='diff_name'),
    path('predict/<str:ticker>', views.predict_future_price, name="price_prediction"),
    path('basic/<str:start_date>/<str:ticker>', views.get_basic_info, name="get_basic"),
    path('news/latest/<str:ticker>', views.get_latest_news, name="get_news"),
]
