from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from shop.forms import LoginForm

# Create your views here.
def index(request):
    return render(request, "shop/index.html", {})

def login(request):
    form = LoginForm()
    return render(request, "shop/login.html", {'form': form})

@csrf_protect
def register(request):
    print(request.POST['fullName'])
    return render(request, "shop/login.html", {})