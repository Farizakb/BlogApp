from django.shortcuts import redirect, render
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User

# Create your views here.
def login_req(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        
        user = authenticate(request, username=username,password=password)
        if not user is None:
            login(request, user)
            return redirect("home")
        else:
            return render(request, "account/login.html",{
                "message":"Username ve Passwordu duzgun daxil edin"
            })
    return render(request, "account/login.html")

def register_req(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        first_name = request.POST["firstname"]
        last_name = request.POST["lastname"]
        password = request.POST["password"]
        re_password = request.POST["repassword"]
        
        if password ==re_password:
            if User.objects.filter(username = username).exists():
                return render(request, "account/register.html",{
                "message":"Username artiq movcuddur olunur"
            })
            else:
                if User.objects.filter(email = email).exists():
                    return render(request, "account/register.html",{
                    "message":"Email artiq movcuddur olunur"
                })
                else:
                    user = User.objects.create_user(username = username,password=password,email=email,first_name=first_name,last_name=last_name)
                    user.save()
                    return redirect("login")
                    
        else:
            return render(request, "account/register.html",{
                "message":"parolalar eyni deildir."
            })
    return render(request, "account/register.html")

def logout_req(request):
    logout(request)
    return redirect("home")