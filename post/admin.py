from django.contrib import admin
from .models import Post


class FcuserAdmin(admin.ModelAdmin):
    list_display = ("title", "writer", "registered_date")


admin.site.register(Post, FcuserAdmin)
