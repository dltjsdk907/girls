from django.shortcuts import render

def post_list(request):
    return render(request, 'blog/post_list.html', {}) # render 화면 만들어내라는 명령, 'blog/post_list.html'로 만들라