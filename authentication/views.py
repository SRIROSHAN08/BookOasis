from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .models import User
# Create your views here.
def LoginPage(request):
    
    if request.user.is_authenticated:
        
        return redirect('post/book')
    
    if request.method == "POST":
        user=authenticate(username = request.POST['username'], password = request.POST['password'])
        
        if user is not None:
            
            login(request,user)
            
            return redirect('/post/book/')
        
        else:
            
            context={
                "error":"*Invalid username or password"
            }
            
            return render(request,'login.html',context)
            
    return render(request,'login.html')

def Logoutuser(request):
    
    logout(request)
    
    return redirect('/')

def Register(request):
    
    if request.method == "POST":
        user_check=User.objects.filter(username = request.POST['username'])

        if len(user_check)>0:
            context={
                'error':'username already exists'
            }
            return render(request,'signup.html',context)
        else:
            
            new_user=User( username = request.POST['username'],first_name= request.POST['first_name'],last_name = request.POST['last_name'],email = request.POST['email'],age = request.POST['age'])
            
            new_user.set_password(request.POST['password'])
            
            new_user.save()
            
            return redirect("/")
    
    return render(request,'signup.html')
