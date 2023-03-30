from django.urls import include, re_path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'basic_app'

urlpatterns = [
  re_path(r'login/$',auth_views.LoginView.as_view(template_name='basic_app/login.html'),name='login'),
  re_path(r'logout/$',auth_views.LogoutView.as_view(),name='logout'),
  re_path(r'signup/$',views.SignUp.as_view(),name='signup'),
]
