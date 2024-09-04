from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
    # 字串欄位(CharField, TextField, EmailField, URLField等)，最好只設置 blank=True 而不設置 null=True
    # 非字串型欄位（如 IntegerField, DateTimeField, ForeignKey等)，可設置null=True
    nickname = models.CharField(max_length=20, default="")
    gender_choice = [("M", "男"), ("F", "女")]
    gender = models.CharField(max_length=1, choices=gender_choice, default="M")
    birthday = models.DateField()
    email = models.EmailField(blank=True, default="")
    tel = models.CharField(max_length=10, blank=True, default="")
    create_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} 綽號:{self.nickname}"
