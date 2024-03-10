from django.shortcuts import render
from ecommerceapp.models import Contact,Product,Subcriber,blog
from django.contrib import messages
from math import ceil
def index(request):
    return render(request, "index.html")

def contact(request):
    if request.method =='POST':
        user_frist=request.POST['fname']
        user_last=request.POST['lname']
        user_email=request.POST['email']
        user_phone=request.POST['phone']
        user_address=request.POST['address']
        user_query=request.POST['discription']
        mydata=Contact(frist_name=user_frist,last_name=user_last,email=user_email,mob=user_phone,address=user_address, query=user_query)
        mydata.save()
        messages.success(request,"We will contact you soon!")
    return render(request, "contact.html")

def collections(request):
    allprods=[]
    catprods=Product.objects.values('category','id')
    cats={item['category'] for item in catprods}
    for cat in cats:
        prod=Product.objects.filter(category=cat)
        n=len(prod)
        nSlides=n//4 + ceil((n/4)-(n//4))
        allprods.append([prod,range(1,nSlides),nSlides])
        params={'allprods':allprods}
    return render(request, "about.html",params)


def subscribe(request):
    if request.method =='POST':
       subcriber_detailes=request.POST['emailadd'] 
       userdata=Subcriber(subcriber_detailes=subcriber_detailes)
       userdata.save()
    return render(request,"index.html")


def blogs(request):
    posts=blog.objects.all()
    context={"posts":posts}
    return render(request,'blogs.html',context)

def payment(request):
    return render(request,"payment.html")
        