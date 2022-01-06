from django.db import models
import os
from django.conf import settings
# from board.views import delete

# 게시판 작성을 위한 Post테이블 생성
class Post(models.Model):
    titles = models.CharField(max_length=50)
    contents = models.TextField()
    # 첨부이미지
    # null=True : null을 허용하는 컬럼으로 생성
    # blank=True : 작성시 입력이 없어도 된다(빈값허용)는 의미
    mainphoto = models.ImageField(blank=True, null=True)

    '''
    이 부분이 없으면 게시글 제목이 나오지않고 Post object(1), (2)로 나온다.
    '''
    def __str__(self):
        return self.titles
    
    
    def delete(self, *args, **kargs):
        if self.mainphoto:
            print(settings.MEDIA_ROOT, self.mainphoto.path)
            os.remove(os.path.join(settings.MEDIA_ROOT, self.mainphoto.path))
        super(Post, self).delete(*args, **kargs)