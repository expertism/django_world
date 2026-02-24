from django.shortcuts import render

def login_users(request):
    if request.method == "POST":
        print(request.POST)
    return render(request, 'users/login.html')

# Create your views here.
