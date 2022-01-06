''' ⑤ 관리자모드에 테이블 등록 '''
''' [+] 라이브러리 설치
C:\ProjectRoot> pip3 install pillow '''
from django.contrib import admin
from .models import Post

admin.site.register(Post)

''' ⑥ 마이그레이션
C:\ProjectRoot> python manage.py makemigrations  ⇒ 데이터베이스에 변경이 필요한 사항을 추출
C:\ProjectRoot> python manage.py migrate         ⇒ 데이터베이스에 변경사항을 반영함
'''
''' ⑦ 관리자모드와 슈퍼유저 생성(with 더미 데이터 입력)
C:\02Workspaces\ProjectRoot> python manage.py createsuperuser
    아이디 : popovely
    비번 : 1110

[next] ProjectRoot3/boardApps/views.py '''