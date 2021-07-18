from django import forms
from django.contrib.auth.hashers import check_password

from .models import Duser


class LoginForm(forms.Form):
    userid = forms.CharField(
        error_messages={"required": "아이디를 입력해 주세요."},
        max_length=32,
        label="사용자 이름",
    )
    password = forms.CharField(
        error_messages={"required": "비밀번호를 입력해 주세요."},
        widget=forms.PasswordInput,
        label="비밀번호",
    )

    def clean(self):
        cleaned_data = super().clean()

        userid = cleaned_data.get("userid")
        password = cleaned_data.get("password")

        if userid and password:
            try:
                duser = Duser.objects.get(userid=userid)
            except Duser.DoesNotExist:
                self.add_error("userid", "아이디가 없습니다.")
                return

            if not check_password(password, duser.password):
                self.add_error("password", "비밀번호가 틀렸습니다.")
            else:
                self.userid = userid
                self.id_pk = duser.id
