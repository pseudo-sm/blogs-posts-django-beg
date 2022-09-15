from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import Post,Author
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.

def index(request):
    posts = Post.objects.all().values("id","content",
    "author","create_date_time","author__category",
    "author__gender","title","image")
    print(posts)
    return render(request,"index.html",{"posts":posts})

def search(request):
    return render(request,"search.html")

def search_action(request):
    search_item = request.GET.get("search_item")
    posts = list(Post.objects.filter(author__name__icontains=search_item).values("id","content",
    "author__name","create_date_time","author__category",
    "author__gender","title"))
    return JsonResponse({"filtered_results":posts})

def signup(request):
    
    return render(request,"signup.html")

def signin(request):
    
    return render(request,"signin.html")


def signup_action(request):
    username = request.POST.get("email")
    password = request.POST.get("password")
    name = request.POST.get("name")
    user = User.objects.create_user(username=username,
    password=password,first_name=name)
    auth.login(request,user)
    return redirect('index')


def signin_action(request):
    username = request.POST.get("email")
    password = request.POST.get("password")
    print(username,password)
    user = auth.authenticate(request,username=username,
    password=password)
    auth.login(request,user)
    return redirect('index')