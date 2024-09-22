# Create your views here.
from django.shortcuts import render,HttpResponse
from blog.models import Category, Post, CustomAutoPrimaryKeyField
from django import forms
from django.contrib.auth.models import Group
# from .forms import NewCommentForm, PostSearchForm
from django.views.generic import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
# import math
# from itertools import chain
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout,update_session_auth_hash
# from math import random
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect,HttpResponsePermanentRedirect, redirect
from django.contrib.auth.forms import UserCreationForm
# from .forms import SignUpForm, LoginForm, PostForm
from django.contrib import messages
from django.contrib.auth import  authenticate,login,logout
# import time
from initiatives.models import Initiative
from impact_stories.models import Stories,DriveImage
from volunteers.models import Ministry
  #


def home(request):
    # last 4 updates
    updates = Post.objects.all().order_by('-publish')[:4]
    # initiatives = Initiative.objects.all() [:10]
    # initiatives = Initiative.objects.filter(status='published')
    initiatives = Initiative.objects.filter(status='published')
    stories = Stories.objects.filter(status='published')
    ministry = Ministry.objects.all()
    # data
    data = {'updates':updates,'initiatives':initiatives,'stories':stories,'ministry':ministry,}
    return render(request, "blog/index.html",data)

def what_we_do1(request):
    return render(request,'our_work/educational.html')

def what_we_do2(request):
    return render(request,'our_work/moral.html')

def what_we_do3(request):
    return render(request,'our_work/mental.html')

def what_we_do4(request):
    return render(request,'our_work/cultural.html')

def post(request, url):
    remaining_categoreis = Category.objects.all()[::-1]
    post = Post.objects.filter(url=url).first()
    cats = Category.objects.all()
    datetime = Post.objects.all()   

    # view count on each blog
    blog_object=Post.objects.get(url=url)
    blog_object.blog_views=blog_object.blog_views+1
    value = str(blog_object.blog_views)
    if value.isdigit():
        value_int = int(value)
        if value_int > 1000000:
            value = "%.1f%s" % (value_int/1000000.00, 'M')
        else:
            if value_int > 1000:
                value = "%.1f%s" % (value_int/1000.0, 'k')
    # print(value)
    blog_object.save()


    latest = Post.objects.all().order_by('-publish')[:4]

    data = {'post':post,'cats':cats,'datetime':datetime,'user': request.user,'value':value,'latest':latest,}
    data_final = data
    return render(request, 'blog/post.html', data_final)



def category_page(request):
    # Get all categories
    categories = Category.objects.all()
    
    # For each category, fetch up to 4 posts
    category_posts = {}
    for category in categories:
        category_posts[category] = Post.objects.filter(category=category).order_by('-publish')[:4]

    context = {
        'categories': categories,
        'category_posts': category_posts,
    }
    return render(request, 'blog/category.html', context)


    
def category(request, url):
    all_categories = Category.objects.all()
    first_4_categories = Category.objects.all()[0:4]
    remaining_categoreis = Category.objects.all()[::-1]
    cats = Category.objects.all()
    
    cat = Category.objects.get(url=url)
    posts_ard = Post.objects.filter(category=cat)
    posts = posts_ard[3::]
    try:
        p1 = posts_ard[0:3]
        # print('p1',p1)
    except:
        p1 = None

    # comments = post.comments.filter(status=True)
    # allcomments = post.comments.filter(status=True)
    page = request.GET.get('page', 1)
    paginator = Paginator(posts, 10)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    data =  {'cat': cat,'cat_4': first_4_categories,'cat_r':remaining_categoreis, 'posts': posts,'p1':p1,'cats':cats}
    return render(request, "blog/category.html",data)

