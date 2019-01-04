from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','title']  # 모델페이지에서 어떤 것들 표시할 건지
    list_display_links = ['title'] # 타이틀에도 링크 걸어줌
    search_fields = ['title']      # 타이틀을 통해 검색기능 추가