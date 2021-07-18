from django.contrib import admin

from duser.models import Duser


class FcuserAdmin(admin.ModelAdmin):
    list_display = ("userid", "useremail", "password", "registered_date")


admin.site.register(Duser, FcuserAdmin)
