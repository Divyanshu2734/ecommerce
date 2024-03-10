from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def signup(request):
 if request.method=="POST":
  user_email= request.POST.get('useremail')
  user_password=request.POST.get('userpassword')
  conf_password=request.POST.get('confpassword')
  if user_password!=conf_password:
    messages.warning(request,"Password is incorrect")
    return redirect("/authapp/signup/")
  person=User.objects.create_user(user_email,user_email,user_password)
  person.save()
  messages.success(request,"signup successfully")
  return redirect("/authapp/login/")
 

 return render(request, "authapps/signup.html")


def handlelogin(request):
  if request.method =='POST':
    user_name=request.POST['useremail']
    user_password=request.POST['userpassword']
    myuser=authenticate(username=user_name,password=user_password)
    if myuser is not None:
     login(request,myuser)
     messages.success(request,"login successfully")
     return redirect("/")
    else:
     messages.warning(request,"invalid credantial")
     return redirect("/authapp/signup/")
    
  
  
  return render(request, "authapps/login.html")

def handlelogout(request):
 logout(request)
 messages.success(request,"logout successfully")
 return redirect("/authapp/login/")
