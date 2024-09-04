from django.contrib import admin
from .models import UserProfile

# Register your models here.


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user_username", "nickname", "gender", "email", "create_time")
    list_filter = ("gender",)
    search_fields = ("nickname",)
    ordering = "create_time"

    # self為UserProfile，obj為其實體物件
    def user_username(self, obj):
        return obj.user.username


admin.site.register(UserProfile, UserProfileAdmin)
