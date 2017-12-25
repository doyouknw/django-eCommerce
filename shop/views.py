from django.shortcuts import render

# Create your views here.
def index(request):
    if request.user.is_authenticated():
        username = request.user.username
        return render(request, "index.html", {'username' : username})
    return render(request, "index.html", {})
