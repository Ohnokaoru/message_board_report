from django.db import models
from userprofile.models import UserProfile


# Create your models here.
# 發文
class BoardUnit(models.Model):
    subject = models.CharField(max_length=20, default="")
    text = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    userprofile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.userprofile.nickname} {self.subject}"


# 留言
class Comment(models.Model):
    # 多個comment會指向同一個board_unit，反查為comments
    board_unit = models.ForeignKey(
        BoardUnit, related_name="comments", on_delete=models.CASCADE
    )
    # 多個self->comment，會指向同一個parent
    parent = models.ForeignKey(
        "self", null=True, blank=True, related_name="replies", on_delete=models.CASCADE
    )
    text = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    userprofile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.userprofile.nickname}針對 {self.board_unit} {self.parent}留言:{self.text[:5]}"
