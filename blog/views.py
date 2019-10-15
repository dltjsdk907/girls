# import 되는 것들도 확인하기
from django.shortcuts import render
from django.utils import timezone
from .models import Post # 같은 폴더에 있는 models.py 에서 가져옴 => .models에서 .은 같은 폴더다라는 의미

def post_list(request):
    # views.post_list 함수는 이제 DB에서 필요한 데이터를 가져와서
    # post_list.html에게 넘겨줘야 함
    # 게시일자가 지금보다 이전으로 들어있는 행만 검색                        '-published_date' 역순
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render( # render() 함수를 호출하여 화면을 출력 - 'blog/post_list.html'로
                request, # 함수에게 사용자가 요청한 정보를 전달
                'blog/post_list.html', # 화면 출력 주체 지정
                {'posts': posts}) # 화면 출력에 사용할 데이터 전달
