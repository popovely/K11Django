''' ③ 관리자모드(Admin site)에 테이블 반영하기 '''
from django.contrib import admin
from books.models import Book, Author, Publisher

# admin페이지에 보이도록 등록
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Publisher)

''' ④ 실제 DB에 반영되도록 마이그레이트 한다.

    C:\ProjectRoot> python manage.py makemigrations  ⇒ 데이터베이스에 변경이 필요한 사항을 추출
    C:\ProjectRoot> python manage.py migrate         ⇒ 데이터베이스에 변경사항을 반영함
    
[next] ProjectRoot/DjangoApps/urls.py '''