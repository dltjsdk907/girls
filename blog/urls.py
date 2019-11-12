from django.urls import path
from . import views  # urls가 있는 파일안에서(.) views를 가져와라

urlpatterns = [
    path('', views.post_list, name='post_list'),
# 주소를 제거하고 나머지 url, 실행할 함수, 그 url을 처리하기로 약속해놓은 함수이름
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'), # name='post_new' URL이 리버스매칭 할 때 씀! (역순!)
                                                       # 주소창에 주소를 쳐서 'post/new'로 찾아서 뒤에를 실행함(정순)
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]