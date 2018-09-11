# from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect, reverse
# from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login


# def login(request):
#     # context = "test"
#     return render(request, "login/login.html")

def do_login(request):
    print("11111111111")
    if request.method == 'GET':
        print("22222222")
        return render(request, 'login/login.html')

    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect(reverse('login'))
    else:
        return render(request, 'login/login.html', {
            'username': username,
            'password': password,
        })
