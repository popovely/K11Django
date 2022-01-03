# 방법2 : 2개의 파일에 작성
from django.urls import path
from . import views

# app_name은 차후 URL처리를 위한 네임스페이스로 활용된다.
app_name = 'livepolls'

# Url패턴이 변경되면 해당 네임스페이스만 변경하면 모두 적용됨.
# 네임스페이스로 처리되므로 livepolls/를 제외한 URL패턴을 기술하면 된다.
urlpatterns = [
    path('', views.index, name="index"),
    path('<int:question_id>/', views.detail, name='detail'), # /livepolls/일련번호/  의 형태
    path('<int:question_id>/results/', views.results, name='results'), # /livepolls/일련번호/results  의 형태
    path('<int:question_id>/vote/', views.vote, name='vote'), # /livepolls/일련번호/vote  의 형태
]
