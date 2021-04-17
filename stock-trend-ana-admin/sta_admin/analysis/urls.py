__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '2/4/2021 11:01 AM'

from django.urls import path, register_converter
from . import converters, views

register_converter(converters.FloatUrlParameterConverter, 'float')

urlpatterns = [
    path('', views.index, name='index'),
    path('test/', views.test, name='index'),
    path('error/', views.bad_request, name='diff_name'),
    path('predict/<str:ticker>', views.predict_future_price, name="price_prediction"),
    path('basic/<str:start_date>/<str:ticker>', views.get_basic_info, name="get_basic"),
    path('calculator/<str:ticker>/<float:cost_price>/<int:amount>', views.get_net_price, name="get_net_price"),
    path('candle/<str:start_date>/<str:ticker>', views.get_candle_render_data, name="candle_chart"),
    path('news/latest/<str:ticker>', views.get_latest_news, name="get_news"),
    path('emotion/today/<str:ticker>', views.get_todays_emotion, name="cal_proportion"),
    path('index/latest/<str:ticker>', views.get_latest_index, name="get_index"),
]
