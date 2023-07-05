from django.shortcuts import render,redirect
from django.http import HttpResponse
from bookapp.models import acdb,apdb,gndb
from userapp.models import carttdb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages
def homepage(request):
    return render(request,"homepage.html")

def addcategory(request):
    return render(request,"1add category.html")

def savecategory(request):
    if request.method=="POST":
        na=request.POST.get('categoryname')
        des=request.POST.get('description')
        img=request.FILES['imagee']
        obj=acdb(categoryname=na,description=des,imagee=img)
        obj.save()
        messages.success(request, "Congratulations..! your Category added successfull..!")
        return redirect(addcategory)

def displaycategory(request):
    data=acdb.objects.all()
    return render(request,"2display category.html",{"data":data})

def editcategory(request,dataid):
    data=acdb.objects.get(id=dataid)
    print(data)
    return render(request,"3edit category.html",{"data":data})

def updatecategorye(request,dataid):
    if request.method=="POST":
        na = request.POST.get('categoryname')
        des = request.POST.get('description')
    try:
        img=request.FILES['imagee']
        fs=FileSystemStorage()
        file=fs.save(img.name,img)
    except MultiValueDictKeyError:
        file=acdb.objects.get(id=dataid).imagee
    acdb.objects.filter(id=dataid).update(categoryname=na,description=des)
    return redirect(displaycategory)

def deletecategory(request,dataid):
    data=acdb.objects.filter(id=dataid)
    data.delete()
    return redirect(displaycategory)


def genres(request):
    return render(request,"Genres.html")

def savegenres(request):
    if request.method=="POST":
        gen=request.POST.get("genres")
        obj=gndb(GenreName=gen)
        obj.save()
        messages.success(request, "Congratulations..! Your Genre added Successfully..!")
        return redirect(genres)

def displaygenres(request):
    gen = gndb.objects.all()
    return render(request,"Display Genres.html",{"gen":gen})

def deletegenres(request,dataid):
    data=gndb.objects.filter(id=dataid)
    data.delete()
    return redirect(displaygenres)

def addproduct(request):
    data = acdb.objects.all()
    Data= gndb.objects.all()
    return render(request,"4add product.html",{"data":data,"Data":Data})

def saveproduct(request):
    if request.method=="POST":
        na=request.POST.get("Name")
        cat=request.POST.get("Categoryname")
        prc=request.POST.get("Price")
        autr=request.POST.get("Author")
        autrlink=request.POST.get("AuthorLink")
        pub=request.POST.get("Publisher")
        date=request.POST.get("Date")
        gen=request.POST.get("Genres")
        lng=request.POST.get("Language")
        rate=request.POST.get("Rating")
        pg=request.POST.get("Page")
        abt=request.POST.get("About")
        img=request.FILES["Imagee"]
        pdf=request.FILES["Pdf"]
        obj=apdb(Name=na,Categoryname=cat,Genres=gen,Price=prc,Author=autr,AuthorLink=autrlink,Publisher=pub,Date=date,Language=lng,Rating=rate,Page=pg,About=abt,Imagee=img,Pdf=pdf)
        obj.save()
        messages.success(request, "Congratulations..! Your Product added Successfully..!")
        return redirect(addproduct)

def displayproduct(request):
    data = apdb.objects.all()
    return render(request,"5display product.html",{"data":data})

def editproduct(request,dataid):
    Data= gndb.objects.all()
    data=apdb.objects.get(id=dataid)
    print(data)
    category_data = acdb.objects.all()
    return render(request,"6edit product.html",{"data":data,"category_data":category_data,"Data":Data})

def updateproduct(request,dataid):
    if request.method=="POST":
        ne = request.POST.get("Name")
        cat = request.POST.get("Categoryname")
        autr = request.POST.get("Author")
        autrlink = request.POST.get("AuthorLink")
        pub = request.POST.get("Publisher")
        date = request.POST.get("Date")
        gen = request.POST.get("Genres")
        lng=request.POST.get("Language")
        prc = request.POST.get("Price")
        rate = request.POST.get("Rating")
        pg = request.POST.get("Page")
        abt = request.POST.get("About")
    try:
        img=request.FILES['Imagee']
        fs=FileSystemStorage()
        file=fs.save(img.name,img)
    except MultiValueDictKeyError:
        file=apdb.objects.get(id=dataid).Imagee
    apdb.objects.filter(id=dataid).update(Name=ne,Categoryname=cat,Author=autr,AuthorLink=autrlink,Language=lng,Publisher=pub,Date=date,Genres=gen,Price=prc,Rating=rate,Page=pg,About=abt)
    return redirect(displayproduct)

def deleteproduct(request,dataid):
    data=apdb.objects.filter(id=dataid)
    data.delete()
    return redirect(displayproduct)

def cartdisplay(request):
    cart=carttdb.objects.all()
    return render(request,"8cart.html",{"cart":cart})

def deletecart(request,dataid):
    data=carttdb.objects.filter(id=dataid)
    data.delete()
    return redirect(cartdisplay)

def loginpage(request):
    return render(request,"7admin login.html")

def adminlogin(request):
    if request.method=="POST":
        username_r=request.POST.get('username')
        password_r=request.POST.get('password')
        if User.objects.filter(username__contains=username_r).exists():
            user=authenticate(username=username_r,password=password_r)
            if user is not None:
                login(request,user)
                request.session['username']=username_r
                request.session['password']=password_r
                return redirect(homepage)
            else:
                return redirect(loginpage)
        else:
            return redirect(loginpage)

def adminlogout(request):
    del request.session['username']
    del request.session['password']
    return redirect(loginpage)
