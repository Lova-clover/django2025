from django.shortcuts import render

def mainpage(request):
    return render(request, 'pages/mainpage.html')

def company(request):
    return render(request, 'pages/company_info.html')

def login_view(request):
    return render(request, 'pages/login.html')

def signup_view(request):
    return render(request, 'pages/signup.html')
