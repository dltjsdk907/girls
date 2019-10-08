# from django.contrib import admin
# from django.urls import path
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]

from django.contrib import admin
from django.urls import path, include
# from . import views                           # !!!

urlpatterns = [
    # path('', views.homepage, name='home'),    # !!!
    path('admin/', admin.site.urls),
    path('', include('blog.urls')), # 마지막에 장고걸스랑 동일하게 하려고 수정한 부분
]