from django.shortcuts import render, redirect
from .models import BoardUnit
from django.contrib.auth.decorators import login_required
from .forms import BoardUnitForm


# Create your views here.


# 新增發文
@login_required
def create_boardunit(request):
    message = ""
    boardunitform = None
    if request.method == "POST":
        form = BoardUnitForm(request.POST)

        if form.is_valid():
            boardunitform = form.save(commit=False)
            # 手動抓取目前帳號user的基本資料
            boardunitform.userprofile = request.user.userprofile
            boardunitform.save()
            message = "新增發文"

        else:
            message = "資料錯誤"

    else:
        form = BoardUnitForm()

    return render(
        request,
        "boardunit/create-boardunit.html",
        {"message": message, "boardunitform": boardunitform, "form": form},
    )
