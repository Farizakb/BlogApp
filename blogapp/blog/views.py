from django.shortcuts import HttpResponse, render
from .models import Blog,Catagory


data = {
    "blogs":[
        {
           "id":1,
           "title":"Web gelistirme kursu",
           "image":"1.jpg",
           "is_active":True,
           "is_home":False ,
           "description":"Gozel bir kurs" 
        },
        {
           "id":2,
           "title":"Python  kursu",
           "image":"2.jpg",
           "is_active":True,
           "is_home":True,
           "description":"Gozel bir kurs" 
        },
        {
           "id":3,
           "title":"Django  kursu",
           "image":"3.jpg",
           "is_active":False,
           "is_home":True,
           "description":"Gozel bir kurs" 
        },
        {
           "id":4,
           "title":"NodeJS  kursu",
           "image":"4.jpg",
           "is_active":False,
           "is_home":True,
           "description":"Gozel bir kurs" 
        },
    ]
}

# Create your views here.
def index(request):
    
    contex = {
        "blogs":Blog.objects.filter(is_home=True),
        "catagories":Catagory.objects.all()
    }
    return render(request,"blog/index.html",contex)

def blogs(request):
    contex = {
        "blogs":Blog.objects.all(),
        "catagories":Catagory.objects.all()
        
    }
    return render(request,"blog/blogs.html",contex)


def blog_det(request,slug):
    currentBlog = Blog.objects.get(slug = slug)
    return render(request,"blog/blog_det.html",{
        "blog":currentBlog
    })
    
    
def catagory(request,slug):
    contex = {
        "blogs":Catagory.objects.get(slug = slug).blog.all(),
        "catagories":Catagory.objects.all(),
        "selected_catagory":slug
        
    }
    return render(request,"blog/blogs.html",contex)

