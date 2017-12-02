from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from accounts.forms import LoginForm

# Create your views here.

def login(request):
    form = LoginForm()
    return render(request, "login.html", {'form': form})

@csrf_protect
def register(request):
    print(request.POST['fullName'])
    return render(request, "login.html", {})