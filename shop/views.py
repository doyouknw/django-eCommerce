from django.shortcuts import render

# Create your views here.
def index(request):
    if request.user.is_authenticated():
        return render(request, "index.html", {})
    return render(request, "index.html", {})
