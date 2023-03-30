from django.urls import include, re_path
from . import views

app_name = 'explore'

urlpatterns = [
    re_path(r'^$',views.Predictor,name='pred'),
    re_path(r'result/$',views.formInfo,name='result'),
]
