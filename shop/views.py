from django.shortcuts import render
from django.views.generic import TemplateView
from products.models import (Product, Category)

# Create your views here.
# def index(request):
#     if request.user.is_authenticated():
#         return render(request, "index.html", {})
#     return render(request, "index.html", {})
class Home(TemplateView):
    template_name = "index.html"
    products = Product.objects.all()

    def get(self, request):
        search = request.GET.get('s')
        if search:
            self.products = self.products.filter(product_name=search)
        context = {
            "products" : self.products,
        }
        return render(request, self.template_name, context)