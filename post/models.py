from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=128, verbose_name="제목")
    writer = models.ForeignKey(
        "duser.Duser", on_delete=models.CASCADE, verbose_name="작성자"
    )
    imagesrc = models.CharField(max_length=512, verbose_name="이미지주소")
    contents = models.TextField(verbose_name="내용")
    tags = models.ManyToManyField("tag.Tag", verbose_name="태그 ")
    registered_date = models.DateTimeField(auto_now_add=True, verbose_name="작성일")

    def __str__(self):
        return self.title

    class Meta:
        db_table = "post"
        verbose_name = "포스트"
        verbose_name_plural = verbose_name
