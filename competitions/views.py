from django.shortcuts import render, HttpResponseRedirect
from .models import Product, TicketOrder
from .forms import CompForm

# this one also needs a reference to the pk
def comp_detail(request, product_id):
    product = Product.objects.get(pk=product_id)
    return render(request, "comp_detail.html", {'product': product})


def currentcomps(request):
    product_list = Product.objects.all()
    context =  {"product_list": product_list}
    return render(request, "currentcomps.html", context)


def related(request):
    product_list = Product.objects.all()
    context = {"product_list": product_list}
    return render(request, "related.html", context)


def winners(request):
    return render(request, "winners.html")


def createcomp(request):
    submitted = False
    if request.method == "POST":
        form = CompForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/createcomp?submitted=True')
    else:
        form = CompForm
        if 'submitted' in request.GET:
            submitted = True
            
    return render(request, "createcomp.html", {'form':form, 'submitted':submitted} )


def my_competitions(request):
    if request.user.is_authenticated:
        me = request.user.id
        products = Product.objects.filter(owner=me)
        context = {"products":products}
        return render(request, "my_competitions.html", context)

    else:
        messages.success(request, ("Login to see your competitions"))
        return redirect('current-comps')



def my_tickets(request):
    if request.user.is_authenticated:
        me = request.user.id
        tickets = TicketOrder.objects.filter(customer=me)
        context = {"tickets":tickets}
        return render(request, "my_tickets.html", context)

    else:
        messages.success(request, ("Login to see your competitions"))
        return redirect('current-comps')


def latest(request):
    latest = Product.objects.all().first
    context =  {"latest": latest}
    return render(request, "latest.html", context)


def related(request):
    product_list = Product.objects.all()
    context = {"product_list": product_list}
    return render(request, "related.html", context)


def winners(request):
    return render(request, "winners.html")


def createcomp(request):
    submitted = False
    if request.method == "POST":
        form = CompForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/createcomp?submitted=True')
    else:
        form = CompForm
        if 'submitted' in request.GET:
            submitted = True
            
    return render(request, "createcomp.html", {'form':form, 'submitted':submitted} )


def my_competitions(request):
    if request.user.is_authenticated:
        me = request.user.id
        products = Product.objects.filter(owner=me)
        context = {"products":products}
        return render(request, "my_competitions.html", context)

    else:
        messages.success(request, ("Login to see your competitions"))
        return redirect('current-comps')



def my_tickets(request):
    if request.user.is_authenticated:
        me = request.user.id
        tickets = TicketOrder.objects.filter(customer=me)
        context = {"tickets":tickets}
        return render(request, "my_tickets.html", context)

