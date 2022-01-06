''' ⑧ 게시판 첫화면과 리스트
[next] ProjectRoot3/boardApps/templates/board/index.html
       ProjectRoot3/boardApps/templates/board/list.html '''
from django.shortcuts import render
from django.shortcuts import redirect
from .models import Post

def index(request):
    return render(request, 'board/index.html')

def list(request):
    postlist = Post.objects.all().order_by('-id')
    return render(request, 'board/list.html', {'postlist':postlist})