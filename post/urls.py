from django.urls import path
from . import views

app_name = "post"

urlpatterns = [
    path("", views.post_list, name="post_list"),
    path("list/", views.post_list, name="post_list"),
    path("detail/<int:pk>", views.post_detail, name="post_detail"),
    path("upload/", views.post_upload, name="post_upload"),
]
