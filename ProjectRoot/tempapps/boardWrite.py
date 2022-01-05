from django import forms

# 게시판의 글쓰기 페이지 UI구현
class BoardWriteForm(forms.Form):
    '''
    ① attrs 속성으로 각 폼에 class를 부여한다.
    ② 가로 사이즈 조정을 위해 w100 / w200 클래스가 추가되었다. (부트스트랩꺼 아님! 걍 사용자지정)
    ③ 첨부파일의 경우 필수사항이 아니므로 required=False를 추가한다.
    ④ 입력폼의 타이틀 부분을 한글로 처리하기 위해 label을 추가한다.
    '''
    user_name = forms.CharField(
        label='작성자',
        widget=forms.TextInput(attrs={'class':'form-control w100', 'id':'user_name'})
    )
    user_pwd = forms.CharField(
        label='패스워드',
        widget=forms.PasswordInput(attrs={'class':'form-control w200', 'id':'user_pwd'})
    )
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(attrs={'class':'form-control'})
    )
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(attrs={'class':'form-control'}))
    file = forms.FileField(label='첨부파일', required=False)