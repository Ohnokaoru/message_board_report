from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm


# Create your views here.


# 建立基本資料
@login_required
def create_userprofile(request):
    message = ""
    userprofileform = None

    try:
        userprofile = UserProfile.objects.get(user=request.user)
        message = "你已經建立過基本資料"

    except UserProfile.DoesNotExist:
        if request.method == "POST":
            form = UserProfileForm(request.POST)

            if form.is_valid():
                userprofileform = form.save(commit=False)
                userprofileform.user = request.user
                userprofileform.save()
                message = "新增基本資料成功"

            else:
                message = "資料 錯誤"
        else:
            form = UserProfileForm()

    return render(
        request,
        "userprofile/create-userprofile.html",
        {"message": message, "form": form, "userprofileform": userprofileform},
    )
