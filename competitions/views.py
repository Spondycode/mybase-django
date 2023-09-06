from django.shortcuts import render

# this one also needs a reference to the pk
def comp_detail(request):
    return render(request, "comp_detail.html", {})


def currentcomps(request):
    return render(request, "currentcomps.html")


def related(request):
    return render(request, "related.html")


def winners(request):
    return render(request, "winners")
