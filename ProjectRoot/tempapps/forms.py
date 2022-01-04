from django import forms
'''
장고에서 제공하는 Form기능을 사용하려면 우선 forms.Form클래스를 상속한다.
각 변수명은 해당 input태그의 name속성값으로 사용된다.
태그 생성시 required속성이 포함되어 기본적인 빈값검증(유효성 검증)을 하게된다.
'''
class QuestionForm(forms.Form):
    '''
    <input type=text를 생성.
        label은 타이틀로 사용.
        max_length : 최대 글자수
    '''
    user_id = forms.CharField(label='아이디', max_length=10)
    # 가장 기본적인 input태그를 생성. label지정을 안했으므로 타이틀은 title로 표시됨.
    title = forms.CharField()
    # 여러줄의 텍스트를 입력할 수 있는 <textarea를 생성.
    content = forms.CharField(widget=forms.Textarea)
    # 기본적인 input 태그를 생성하되 type='email'로 생성.
    email = forms.EmailField()
    '''
    <input type=checkbox 를 생성.
        required=False : 유효성 검증을 하지 않겠다는 뜻.
    '''
    my_check = forms.BooleanField(required=False)