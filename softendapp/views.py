from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        # ตรวจสอบรหัสผ่านว่าตรงกัน
        if password != confirm_password:
            messages.error(request, 'Passwords do not match!')
            return redirect('register')

        # ตรวจสอบว่าผู้ใช้งานมีอยู่แล้วหรือไม่
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists!')
            return redirect('register')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists!')
            return redirect('register')

        # สร้างผู้ใช้งานใหม่
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, 'Account created successfully!')
        return redirect('login')
    return render(request, 'register.html')