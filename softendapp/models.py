from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_groups",  # แก้ไข related_name
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_permissions",  # แก้ไข related_name
        blank=True,
    )

    def __str__(self):
        return self.username

# โมเดลสำหรับโน้ต
class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')  # ความสัมพันธ์กับ User
    title = models.CharField(max_length=255)
    content = models.TextField()
    color_code = models.CharField(max_length=7, default='#FFFFFF')  # รหัสสีเริ่มต้นเป็นสีขาว
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
