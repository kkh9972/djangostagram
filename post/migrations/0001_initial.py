# Generated by Django 2.2.1 on 2021-07-11 14:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("tag", "0001_initial"),
        ("duser", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=128, verbose_name="제목")),
                ("imagesrc", models.CharField(max_length=128, verbose_name="이미지주소")),
                ("contents", models.TextField(verbose_name="내용")),
                (
                    "registered_date",
                    models.DateTimeField(auto_now_add=True, verbose_name="작성일"),
                ),
                ("tags", models.ManyToManyField(to="tag.Tag", verbose_name="태그 ")),
                (
                    "writer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="duser.Duser",
                        verbose_name="작성자",
                    ),
                ),
            ],
            options={
                "verbose_name": "포스트",
                "verbose_name_plural": "포스트",
                "db_table": "post",
            },
        ),
    ]
