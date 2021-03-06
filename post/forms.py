from django import forms


class PostForm(forms.Form):
    title = forms.CharField(
        error_messages={"required": "제목을 입력해 주세요."},
        max_length=128,
        label="제목",
    )
    imagesrc = forms.CharField(
        error_messages={"required": "이미지주소를 입력해 주세요."},
        max_length=128,
        label="이미지주소",
    )
    contents = forms.CharField(
        error_messages={"required": "내용을 입력해 주세요."},
        widget=forms.Textarea,
        label="내용",
    )
    tags = forms.CharField(required=False, label="태그")
