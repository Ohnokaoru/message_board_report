from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm


# Create your views here.


# 建立基本資料
@login_required
def create_userprofile(request):
    message = ""

    try:
        userprofile = UserProfile.objects.get(user=request.user)
        return redirect("review-userprofile")

    except UserProfile.DoesNotExist:
        if request.method == "POST":
            form = UserProfileForm(request.POST)

            if form.is_valid():
                userprofileform = form.save(commit=False)
                userprofileform.user = request.user
                userprofileform.save()
                return redirect("review-userprofile")

            else:
                message = "資料錯誤"
        else:
            form = UserProfileForm()

    return render(
        request,
        "userprofile/create-userprofile.html",
        {"message": message, "form": form},
    )


# 檢視基本資料
@login_required
def review_userprofile(request):
    try:
        userprofile = UserProfile.objects.get(user=request.user)

    except UserProfile.DoesNotExist:
        return redirect("create-userprofile")

    return render(
        request, "userprofile/review-userprofile.html", {"userprofile": userprofile}
    )


# 修改
@login_required
def edit_userprofile(request):
    message = ""
    try:
        userprofile = UserProfile.objects.get(user=request.user)

    except UserProfile.DoesNotExist:
        return redirect("review-userprofile")

    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=userprofile)

        if form.is_valid():
            userprofileform = form.save(commit=False)
            userprofileform.user = request.user
            userprofileform.save()
            return redirect("review-userprofile")

        else:
            message = "資料錯誤"

    else:
        form = UserProfileForm(instance=userprofile)

    return render(
        request, "userprofile/edit-userprofile.html", {"form": form, "message": message}
    )
