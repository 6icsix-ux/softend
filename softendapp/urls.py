from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # เส้นทางสำหรับหน้าแรก
    path('login/', views.login, name='login'),  # เส้นทางสำหรับหน้า login
]
