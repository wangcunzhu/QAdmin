from django.shortcuts import render

# Create your views here.

# from django.http import HttpResponse

from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
# from django.contrib.auth import authenticate, login


# def caselist(request):
#     context = dict()
#     context["username"] = "wangcunzhu"
#     return render(request, "casetest/plain_page.html", context)


@login_required(login_url='/login')
def caselist(request):
    return render(request, 'casetest/plain_page.html', {'username': request.user.username})
