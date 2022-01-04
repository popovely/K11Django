from django import forms

# 글쓰기
class BoardWriteForm(forms.Form):
    user_name = forms.CharField(
        label='작성자', max_length=10,
        widget=forms.TextInput(attrs={'class':'form-control', 'id':'user_name'})
    )
    user_pwd = forms.CharField(
        label='패스워드', max_length=20,
        widget=forms.PasswordInput(attrs={'class':'form-control', 'id':'user_pwd'})
    )
    title = forms.CharField(
        label='제목', max_length=50,
        widget=forms.TextInput(attrs={'class':'form-control'})
    )
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(attrs={'class':'form-control'}))
    file = forms.FileField(label='첨부파일', required=False)