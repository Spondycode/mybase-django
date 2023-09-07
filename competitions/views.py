from django.shortcuts import render
from .models import Product

# this one also needs a reference to the pk
def comp_detail(request):
    return render(request, "comp_detail.html", {})


def currentcomps(request):
    product_list = Product.objects.all()
    return render(request, "currentcomps.html", {"product_list": product_list})


def related(request):
    return render(request, "related.html")


def winners(request):
    return render(request, "winners.html")
