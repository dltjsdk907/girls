from django.urls import path
from . import views  # urls가 있는 파일안에서(.) views를 가져와라

urlpatterns = [
    path('', views.post_list, name='post_list'),
        # 주소를 제거하고 나머지 url, 실행할 함수, 그 url을 처리하기로 약속해놓은 함수이름
]