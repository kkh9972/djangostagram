from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect

from duser.forms import LoginForm
from duser.models import Duser


def home(request):
    # return HttpResponse("Home!")
    return redirect("/post/list")


def register(request):
    if request.method == "GET":
        return render(request, "register.html")

    elif request.method == "POST":
        userid = request.POST.get("userid", None)
        useremail = request.POST.get("useremail", None)
        password = request.POST.get("password", None)
        re_password = request.POST.get("re-password", None)

        res_data = {}
        if not (userid and useremail and password and re_password):
            res_data["error"] = "모든 값을 입력해야 합니다."

        elif password != re_password:
            res_data["error"] = "비밀번호가 다릅니다."

        else:
            try:
                duser = Duser.objects.get(userid=userid)
            except Duser.DoesNotExist:
                duser = Duser(
                    userid=userid, useremail=useremail, password=make_password(password)
                )
                duser.save()
                return redirect("/")
            else:
                res_data["error"] = "해당 아이디가 이미 존재합니다."

        return render(request, "register.html", res_data)


def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            # 세션
            request.session["user"] = form.id_pk
            request.session["userid"] = form.userid
            return redirect("/")
    else:
        form = LoginForm()

    return render(request, "login.html", {"form": form})


def logout(request):
    if request.session.get("user"):
        del request.session["user"]

    return redirect("/")
