from django.contrib.auth.decorators import login_required # 로그
from django.shortcuts import render

@login_required # 로그아웃 상태가 되면 setting.LOGIN_URL로 이동시켜 준다.
def profile(request):
    # request.user # django.contrib.auth.models.User 로그인 되어있을 시 로그아웃 AnonymousUser
    return render(request, 'accounts/profile.html')
