from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from account.views import home
from blogs.models import Blog
import datetime

#from .models import blogs

# Create your views here.

def index(request):
    return render(request, "index.html")


def logout(request):
    auth.logout(request)
    return redirect('https://blogging-site-b.herokuapp.com/')


def create(request):
    if(request.method == 'POST' ):
        title = request.POST['title']
        content = request.POST['content']
        delete = False
        username = request.user.username
        form = Blog(title=title, content=content,delete=delete,user=username)
        form.save()
        return render(request, "index.html")
    else:
        return render(request, "create.html")


def read(request):

    allblogs = Blog.objects.all()
    allblogs=allblogs[::-1]
    return render(request, "read.html", {'blogs': allblogs})


def update(request):

    if(request.method == 'POST' ):
        try:
            title = request.POST['title']
            updated_title = request.POST['updated_title']
            updated_content = request.POST['updated_content']
            blog_to_update = Blog.objects.get(user=request.user.username,title=title)
            blog_to_update.title = updated_title
            blog_to_update.content = updated_content
            blog_to_update.save(update_fields=['title','content'])
            return render(request, "index.html")
        except:
            return render(request, "index.html")
    else:
        allblogs = Blog.objects.all()
        allblogs=allblogs[::-1]
        return render(request, "update.html", {'blogs': filter(lambda x: x.user==request.user.username ,allblogs)})


def delete(request):

    if(request.method == 'POST' ):
        title = request.POST['title']
        Blog.objects.filter(user=request.user.username,title=title).delete()
        return render(request, "index.html")
    else:
        allblogs = Blog.objects.all()
        allblogs=allblogs[::-1]
        return render(request, "delete.html", {'blogs': filter(lambda x: x.user==request.user.username ,allblogs)})