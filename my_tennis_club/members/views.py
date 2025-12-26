from django.http import HttpResponse
from django.template import loader
from .models import Member , shopping
from django.shortcuts import render , get_object_or_404

# Create your views here.
def sample(request):
    template = loader.get_template("myfirst.html")
    return HttpResponse(template.render())

def members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template("all_members.html")
    context = {
        'mymembers':mymembers,
    }
    return HttpResponse(template.render(context,request))

def details(request , id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template("details.html")
    context = {
        'mymember':mymember,
    }
    return HttpResponse(template.render(context, request))

def home_page(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())

def product_page(request):
    products = shopping.objects.all()
    # template = loader.get_template('product.html')
    return render(request, 'product.html', {'products':products})

def product_details(request, product_id):
    product = get_object_or_404(shopping , pk= product_id)
    return render(request , 'product_details.html', {'product' : product})