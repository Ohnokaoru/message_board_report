from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import ChaloginForm
from django.contrib.auth import login, logout

# Create your views here.


# 註冊
def user_register(request):
    message = ""
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()

        else:
            message = "資料錯誤:"

    else:
        form = UserCreationForm()

    return render(
        request, "user/user-register.html", {"form": form, "message": message}
    )


# 登入
def chalogin(request):
    message = ""
    form = None
    if request.method == "POST":
        form = ChaloginForm(request, request.POST)

        if form.is_valid():
            # get_user為一種方法，get_user()為取得User的實體物件
            user = form.get_user()

            login(request, user)
            message = "登入成功"

        else:
            message = "資料錯誤"

    else:
        form = ChaloginForm()

    return render(request, "user/chalogin.html", {"message": message, "form": form})


# 登出
def user_logout(request):
    logout(request)

    return redirect("chalogin")
