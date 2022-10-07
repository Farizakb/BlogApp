from django.shortcuts import HttpResponse, render

# Create your views here.
def index(request):
    return render(request,"blog/index.html")

def blogs(request):
    return render(request,"blog/blogs.html")


def blog_det(request,id):
    return render(request,"blog/blog_det.html",{
        "id":id
    })

