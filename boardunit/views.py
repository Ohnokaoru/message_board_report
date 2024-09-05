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

    paginator = Paginator(all_boardunits, 4)

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
    myboardunits = BoardUnit.objects.filter(userprofile=request.user.userprofile)

    if not myboardunits:
        return redirect("create-boardunit")

    paginator = Paginator(myboardunits, 4)

    try:
        page_number = request.GET.get("page", 1)

    except (TypeError, ValueError):
        page_number = 1

    page_obj = paginator.get_page(page_number)

    return render(request, "boardunit/review-myboardunit.html", {"page_obj": page_obj})
