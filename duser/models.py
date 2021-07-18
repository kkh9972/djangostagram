from django.db import models


class Duser(models.Model):
    userid = models.CharField(max_length=32, verbose_name="사용자아이디")
    useremail = models.EmailField(max_length=128, verbose_name="사용자이메일")
    password = models.CharField(max_length=64, verbose_name="비밀번호")
    registered_date = models.DateTimeField(auto_now_add=True, verbose_name="가입일")

    def __str__(self):
        return self.userid + " " + self.useremail

    class Meta:
        db_table = "duser"
        verbose_name = "사용자"
        verbose_name_plural = verbose_name
