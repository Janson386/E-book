from django.shortcuts import render,redirect
from django.http import HttpResponse
from bookapp.models import acdb,apdb,gndb
from userapp.models import custemerdetaildb,carttdb,paymentdetaildb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages



# Create your views here.

def home(request):
    gen = gndb.objects.all()
    data = acdb.objects.all()
    return render(request,"1homepage.html",{"data":data,"gen":gen})

def product(request,itemcat):
    products = apdb.objects.filter(Categoryname=itemcat)
    data = acdb.objects.all()
    gen = gndb.objects.all()
    return render(request,"2product page.html",{"data":data,"products":products,"gen":gen})

def moreproduct(request,itemcat):
    products = apdb.objects.filter(Categoryname=itemcat)
    gen = gndb.objects.all()
    data = acdb.objects.all()
    return render(request,"more product.html",{"data":data,"products":products,"gen":gen})

def genres(request,itemcat):
    products = apdb.objects.filter(Genres=itemcat)
    gen = gndb.objects.all()
    data = acdb.objects.all()
    return render(request,"2product page.html",{"data":data,"products":products,"gen":gen})

def singleproduct(request,dataid):
    product = apdb.objects.get(id=dataid)
    # proo = acdb.objects.get(id=dataid)
    gen = gndb.objects.all()
    data = acdb.objects.all()
    return render(request,"4single.html",{"data":data,"product":product,"gen":gen})

def demo(request):
    gen = apdb.objects.all()
    return render(request,"demo.html",{"gen":gen})

def cart(request):
    cart = carttdb.objects.filter(user=request.session['usernamel'])
    return render(request,"5cart.html",{"cart":cart})

def savecart(request):
    if request.method=="POST":
        un = request.POST.get('user')
        na =request.POST.get('productname')
        pp = request.POST.get('productprice')
        pl =request.POST.get('productlanguage')
        pdf =request.FILES['pdf']
        obj=carttdb(productname=na,productprice=pp,user=un,productlanguage=pl,pdf=pdf)
        obj.save()
        messages.success(request, "Congratulations..! Your Order is Successfully..!")
        return redirect(home)

def Deletecart(request,dataid):
    data=carttdb.objects.filter(id=dataid)
    data.delete()
    return redirect(cart)

def checkout(request):
    return render(request,"6checkout.html")

def savecheckout(request):
    if request.method=="POST":
        fn =request.POST.get('fullname')
        em = request.POST.get('emaill')
        pn = request.POST.get('phonenumber')
        cty =request.POST.get('city')
        ste =request.POST.get('state')
        obj=paymentdetaildb(fullname=fn,emaill=em,phonenumber=pn,city=cty,state=ste,)
        obj.save()
        return redirect(home)

def userlogin(request):
    return render(request,"7user login.html")

def usersavedata(request):
    if request.method=="POST":
        user_r=request.POST.get('usernamel')
        gmail_r = request.POST.get('email')
        password_r=request.POST.get('passwordl')
        c_password=request.POST.get('conformpasswordl')
        obj=custemerdetaildb(username=user_r,email=gmail_r,password=password_r,conformpassword=c_password)
        obj.save()
        messages.success(request, "Congratulations..! Account Create Successfully..!")
        return redirect(userlogin)

def userloginpage(request):
        if request.method == "POST":
            username_R = request.POST.get('usernamel')
            password_R = request.POST.get('passwordl')
            if custemerdetaildb.objects.filter(username=username_R,password=password_R).exists():
                data=custemerdetaildb.objects.filter(username=username_R,password=password_R).values('email','id').first()

                request.session['usernamel']=username_R

                request.session['passwordl']=password_R

                return redirect(home)
            else:
                  return redirect(userlogin)
        else:
             return redirect(userlogin)

def userlogout(request):
    if request.session:
        request.session.clear()
    return redirect(userloginpage)

def profile(request):
    profile = custemerdetaildb.objects.filter(username=request.session['usernamel'])
    return render(request,"9 profile.html",{"profile":profile})