from django.contrib import admin
from livepolls.models import Question, Choice

# 4. 외래키 관계의 테이블을 한 화면에서 편집
class ChoiceInline(admin.StackedInline):   # 세로형으로 배치
#class ChoiceInline(admin.TabularInline):    # 테이블형(가로형)으로 배치
    model = Choice  # 테이블 선택
    extra = 4   # 입력상자의 개수.
                # 기존에 있던 질문에는 기존 선택사항들이 상단에 입력상자 형태로 먼저 나오고
                # extra의 개수만큼 추가된다.

# 1. 필드순서 변경하기 : 테이블에 적용되진 않고, 관리자모드에서만 순서가 변경됨
'''
class QuestionChanger(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']
'''

# 2. 필드 분리해서 보여주기 + 순서변경
'''
1번과 2번은 동시에 사용하면 에러가 발생하므로 하나만 사용해야 한다.
'''
class QuestionChanger(admin.ModelAdmin):
    fieldsets = [
        ('질문을 입력하세요', {'fields' : ['question_text']}),
        ('날짜를 입력하세요', {'fields' : ['pub_date'], 'classes': ['collapse']}),
    ]
    # 4번 class생성후 설정
    inlines = [ChoiceInline]
# 3. 필드 접기 : 'classes': ['collapse'] 항목을 추가하면 된다.
    
'''
models.py에서 테이블을 생성하면 관리자모드에 적용하기 위해
아래와 같은 등록절차가 필요하다.
'''
admin.site.register(Question, QuestionChanger)
admin.site.register(Choice)
