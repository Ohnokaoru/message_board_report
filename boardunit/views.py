from django.shortcuts import render, redirect
from .models import BoardUnit
from django.contrib.auth.decorators import login_required
from .forms import BoardUnitForm
from django.core.paginator import Paginator

# Create your views here.


# 新增發文
@login_required
def create_boardunit(request):
    message = ""

    if request.method == "POST":
        form = BoardUnitForm(request.POST)

        if form.is_valid():
            boardunitform = form.save(commit=False)
            # 手動抓取目前帳號user的基本資料
            boardunitform.userprofile = request.user.userprofile
            boardunitform.save()
            return redirect("review-all")

        else:
            message = "資料錯誤"

    else:
        form = BoardUnitForm()

    return render(
        request,
        "boardunit/create-boardunit.html",
        {"message": message, "form": form},
    )


# 所有發文(首頁)
def review_all(request):
    all_boardunits = BoardUnit.objects.all().order_by("-time")
    if not all_boardunits:
        return redirect("create-boardunit")

    paginator = Paginator(all_boardunits, 3)

    try:
        page_number = int(request.GET.get("page", 1))

    except (ValueError, TypeError):
        page_number = 1

    page_obj = paginator.get_page(page_number)

    return render(request, "boardunit/review-all.html", {"page_obj": page_obj})


# 點選內文
def review_detail(request, boardunit_id):
    try:
        boardunit = BoardUnit.objects.get(id=boardunit_id)

    except BoardUnit.DoesNotExist:
        return redirect("review-all")

    return render(request, "boardunit/review-detail.html", {"boardunit": boardunit})


# 我的歷史發文
def review_myboardunit(request):
    myboardunits = BoardUnit.objects.filter(
        userprofile=request.user.userprofile
    ).order_by("-time")

    if not myboardunits:
        return redirect("create-boardunit")

    paginator = Paginator(myboardunits, 3)

    try:
        page_number = request.GET.get("page", 1)

    except (TypeError, ValueError):
        page_number = 1

    page_obj = paginator.get_page(page_number)

    return render(request, "boardunit/review-myboardunit.html", {"page_obj": page_obj})


# 修改我的歷史發文
def edit_myboardunit(request, boardunit_id):
    try:
        myboardunit = BoardUnit.objects.get(
            id=boardunit_id, userprofile=request.user.userprofile
        )
    except BoardUnit.DoesNotExist:
        return redirect("review-myboardunit")

    if request.method == "POST":
        form = BoardUnitForm(request.POST, instance=myboardunit)
        if form.is_valid():
            myboardunitform = form.save(commit=False)
            myboardunitform.userprofile = request.user.userprofile
            myboardunitform.save()
            return redirect("review-detail", boardunit_id=boardunit_id)

    else:
        form = BoardUnitForm(instance=myboardunit)

    return render(
        request,
        "boardunit/edit-myboardunit.html",
        {"form": form, "myboardunit": myboardunit},
    )
