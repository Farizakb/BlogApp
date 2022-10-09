from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('home',views.index, name='home'),
    path('blogs',views.blogs, name='blogs'),
    path('catagory/<slug:slug>',views.catagory, name = "catagory"),
    path('blogs/<slug:slug>',views.blog_det, name='blog_det'),
]
