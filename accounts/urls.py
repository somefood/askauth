from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns =[
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'), #template_name을 설정하여 내가 만든 template로 경로 변경
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),
]