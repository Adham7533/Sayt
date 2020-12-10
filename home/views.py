import json
from django.contrib import messages
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from home.models import *

# Create your views here.

def index(request):
    setting=Setting.objects.all()
    post=Post.objects.all()
    page="home"
    context={
        'setting':setting,
        'post':post
    }
    return render(request,'index.html',context)
def post(request):
    post=Post.objects.all()

    return render(request,'post.html',{'post':post})