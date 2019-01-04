from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns =[
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'), #template_name을 설정하여 template 경로 변경
]