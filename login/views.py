# from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
# from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login


# def login(request):
#     # context = "test"
#     return render(request, "login/login.html")

def do_login(request):
    # print("11111111111")
    # print(request.path)
    # if request.method == 'GET':
    #     print("22222222")
    #     return render(request, 'login/login.html')
    print("11111111111")
    username = request.POST.get('username')
    password = request.POST.get('password')
    print(username)
    print(password)
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # return redirect(reverse('login'))
        return render(request, 'casetest/plain_page.html')
    else:
        return render(request, 'login/login.html', {
            'username': username,
            'password': password,
        })
