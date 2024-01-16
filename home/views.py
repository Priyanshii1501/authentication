from django.shortcuts import render , redirect ,  get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , logout, login
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from  .models import UserDb



# Create your views here.
def index(request):
    
    if request.user.is_anonymous:
        return redirect("/login")
    
    users=UserDb.objects.all()
    
    return render(request , 'index.html' , {'users': users} )


@csrf_protect
def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect("/login")
    return render(request, 'login.html')

   

def logoutUser(request):
    logout(request)
    return redirect("/login")

def add_user(request):
    if request.method =="POST":
        

        print("Added")
        user_name=request.POST.get("user_name")
        user_email=request.POST.get("user_email")
        user_phone=request.POST.get("user_phone")
        user_address=request.POST.get("user_address")

        if user_name and user_email:
            UserDb.objects.create(name=user_name , email=user_email , phone=user_phone ,address=user_address)
               
        return redirect('/')
    
    return render(request, 'add_user.html')     


def delete_user(request, user_id):
    user= get_object_or_404(UserDb, pk=user_id)
    user.delete()

    return redirect("/")

def update_user(request , user_id):
    user = get_object_or_404(UserDb, pk=user_id)
    return render(request , "update_user.html" , {'user' : user})

def do_update_user(request , user_id):
    
    user_name=request.POST.get("user_name")
    user_email=request.POST.get("user_email")
    user_phone=request.POST.get("user_phone")
    user_address=request.POST.get("user_address")
    
    user = get_object_or_404(UserDb, pk=user_id)

    user.name=user_name
    user.email=user_email
    user.phone=user_phone
    user.address=user_address
    
    user.save()
    return redirect("/")






