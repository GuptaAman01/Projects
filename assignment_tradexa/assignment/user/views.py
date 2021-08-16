from django.shortcuts import render
from django.http import HttpResponse
from .models import product
from django.contrib.auth.models import User, auth
# Create your views here.

global firstname
global lst
lst = []

def user(request):
    return render(request, 'user.html')

def login(request):
    global firstname
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    email = request.POST['email']
    password = request.POST['password']
    username = request.POST['username']

    user = User.objects.create_user(username = username,password=password, first_name = firstname, last_name = lastname, email=email)
    user.save()
    print("User Created")

    return render(request, 'home.html', {'name': firstname})

def cproduct(request):
    return render(request, 'product.html')

def create(request):
    pname = request.POST['pname']
    price = request.POST['price']
    cat = request.POST['create']
    uat = request.POST['update']

    lst.append(product(pname, price, cat, uat))

    return render(request, 'home.html', {'lst': lst})