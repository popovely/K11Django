''' ④ 테이블 생성
[next] ProjectRoot3\boardApps\admin.py '''
from django.db import models

class Post(models.Model):
    titles = models.CharField(max_length=50)
    contents = models.TextField()
    file = models.FileField(blank=True, null=True)

    ''' 반드시 작성해야 하는 부분 '''
    def __str__(self):
        return self.titles