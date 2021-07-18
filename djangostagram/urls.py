from django.contrib import admin
from django.urls import path, include

from duser.views import home

urlpatterns = [
    path("admin/", admin.site.urls),
    path("user/", include("duser.urls", namespace="duser")),
    path("post/", include("post.urls", namespace="post")),
    path("", home),
]
