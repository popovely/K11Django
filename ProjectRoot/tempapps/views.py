from django.shortcuts import render
from django.http import HttpResponseRedirect
from tempapps.forms import QuestionForm
# 글쓰기 모듈 import
from tempapps.boardWrite import BoardWriteForm

'''
    views에 함수 정의시에
    request 내장객체(를 인자로 받는 것)은 필수요소임
'''
# tempapps의 index 화면 : 바로가기 링크만 있음
def index(request):
    return render(request, 'index.html')

# Template Filter를 사용하기 위한 여러종류의 변수선언 및 Template호출
def templateFilter(request):
    # 정수형 변수
    num1 = 1
    num2 = 10
    # 문자형 변수
    engStr = "nakja's MustHave\r\njava <b>web</b>programming"   # 특수기호, 태그 포함
    hanStr = "낙자쌤의 자바 웹 프로그래밍"
    # 컬렉션(집합/배열)형 변수
    dictVar = {'a':'유비','b':'관우','c':'장비'}    # Dictionary
    listVar = ['손오공', '저팔계', '사요정']        # List
    context = {'num1':num1, 'num2':num2, 'engStr':engStr, 'hanStr':hanStr,
               'dictVar':dictVar, 'listVar':listVar}
    
    # 템플릿 호출 및 값 전달
    return render(request, 'template_filter.html', context)

# 템플릿 태그
def templateTag(request):
    # Dictionary를 인자로 가진 List
    books = [
        {"name":"자바", "price":1000},
        {"name":"HTML", "price":2000},
        {"name":"JSP", "price":3000}
    ]
    # 빈 List
    hobbys = []
    favorites = ['운동', '공부', '여행', '경제']
    iVar = range(1,11)

    context = {'books':books, 'hobbys':hobbys, 'favorites':favorites, 'iVar':iVar}
    return render(request, 'template_tag.html', context)

# 장고의 폼 생성기능 사용하기
def formCreate(request):
    '''
        JAVA에서의 Servlet의 doGet(), doPost()와 같이 하나의 함수에서
        폼 출력과 전송된 값 처리를 동시에 하도록 권장하고 있다.
        즉, POST이면 폼값을 입력한 후 전송할 때의 처리를 한다.
    '''
    if request.method == 'POST':
        # 진입시 전송방식이 POST이면 submit된 폼값을 처리한다.
        form = QuestionForm(request.POST)
        # 폼값의 유효성 검증(빈값검증)을 한다.
        if form.is_valid():
            # 폼 데이터가 유효하면 클린데이터(cleaned_data)로 복사한다.
            user_id = form.cleaned_data['user_id']
            # user_id 외에 title, content도 동일한 방식으로 저장가능.
            
            # 폼 데이터에 문제가 없다면 DB에 입력하거나 비즈니스로직을 수행한다.
            
            # return HttpResponseRedirect('/thanks/')   # 페이지 이동
            return render(request, 'thanks.html', {'user_id':user_id})  # 템플릿 렌더링
    else:
        # 전송방식이 GET이면 입력폼으로 진입한다.
        form = QuestionForm()
    # 입력폼 진입을 위해 템플릿을 렌더링한다.
    return render(request, 'form_create.html', {'form':form})

def thanks(request):
    return render(request, 'thanks.html')
'''
# 글쓰기 (ME)
def boardWrite(request):
    if request.method == 'POST':
        form = BoardWriteForm(request.POST)
        return render(request, 'index.html')
    else:
        form = BoardWriteForm()
        
    return render(request, 'boardWrite.html', {'form':form})
'''
# 글쓰기 (T)
def boardWrite(request):
    if request.method == 'POST':
        template_path = 'boardWrite.html'
    else:
        form = BoardWriteForm()
        template_path = 'boardWrite.html'
    
    # 입력폼 진입을 위해 템플릿을 렌더링한다.
    return render(request, template_path, {'form':form})