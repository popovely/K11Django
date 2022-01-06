''' ③ URL등록 - 애플리케이션 레벨 URLConf 
[next] ProjectRoot3\boardApps\models.py '''
from django.urls import path
from . import views

app_name = 'boardApps'

urlpatterns = [
    path('', views.list, name="list"),
    path('list/', views.list, name="list"),
    # path('view/<int:pk>/', views.view, name="view"),
    # path('write/', views.write, name="write"),
    # path('edit/<int:pk>/', views.edit, name="edit"),
    # path('delete/<int:pk>/', views.delete, name="delete"),
]
