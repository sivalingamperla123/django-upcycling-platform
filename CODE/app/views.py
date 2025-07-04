from django.shortcuts import render,redirect

from . models import *
from django.contrib import messages
# Create your views here.

from django.utils import timezone
from django.db.models import Q

def  index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        dob = request.POST['dob']
        gender = request.POST['gender']
        contact = request.POST['contact']
        address = request.POST['address']
        profile = request.FILES['profile']
        proof = request.FILES['proof']
        
        data = UsersModel.objects.filter((Q(email=email) | Q(contact=contact))).exists()
        if data:
            messages.success(request, 'Email or Contact already existed')
            return redirect('register')
        else:
            UsersModel.objects.create(name=name, email=email, password=password, dob=dob, gender=
                                      gender, contact=contact, address=address, profile=profile,proof=proof).save()
            messages.success(request, 'Registration Successfull')
            return redirect('register')

    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        dat = UsersModel.objects.filter(email=email, status='Accepted').exists()
        if dat:
            data = UsersModel.objects.filter(email=email, password=password).exists()
            if data:
                request.session['email']=email
                request.session['login']='user'
                return redirect('home')
            else:
                messages.success(request, 'Invalid Email or Password')
                return redirect('login')
        else:
            messages.success(request, 'Admin Not Accept Your Registration')
            return redirect('login')
    return render(request, 'login.html')

def adminlogin(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        if email =='admin@gmail.com' and password == 'admin':
            request.session['email'] = email
            request.session['login'] = 'admin'
            return redirect('home')
    return render(request, 'adminlogin.html')


def home(request):
    login = request.session['login']
    return render(request, 'home.html',{'login':login})

def logout(request):
    del request.session['email']
    del request.session['login']
    return redirect('index')

def profile(request):
    login = request.session['login']
    email = request.session['email']
    data = UsersModel.objects.filter(email=email)
    return render(request, 'profile.html',{'login':login,'data':data, 'email':email})


def updateprofile(request):
    login = request.session['login']
    if request.method == 'POST':
        email = request.session['email']
        contact = request.POST['contact']
        address = request.POST['address']
        profile = request.FILES['profile']
        data = UsersModel.objects.get(email=email)
        data.contact = contact
        data.address = address
        data.profile = profile
        data.save()
        return redirect('profile')
    return render(request, 'updateprofile.html',{'login': login})


def uploadproduct(request):
    login = request.session['login']
    if request.method == 'POST':
        name = request.POST['productName']
        category = request.POST['category']
        description = request.POST['description']
        image = request.FILES['image']
        email = request.session['email']
        upload_time = timezone.now()
        data = UploadProductModel.objects.create(
            product_name=name, category=category, 
            product_desc=description, product_img=image, 
            uploaderemail=email, upload_time=upload_time
        )
        data.save()
        messages.success(request, 'Product Uploaded Successfully!')
        return redirect('uploadproduct')

    return render(request, 'uploadproduct.html',{'login':login})

def products(request):
    login = request.session['login']
    email = request.session['email']
    data = UploadProductModel.objects.filter(status='Available')
    return render(request, 'products.html',{'login':login,'data':data,'email':email})


def viewproduct(request,id):
    login = request.session['login']
    useremail = request.session['email']
    print(request.session['email'])
    data = UploadProductModel.objects.filter(id=id)
    return render(request, 'viewproduct.html',{'login':login,'data':data,'useremail':useremail})

    
def books(request):
    login = request.session['login']
    data = UploadProductModel.objects.filter(category='books',status='Available')
    useremail = request.session['email']
    return render(request, 'products.html',{'login':login,'data':data,'useremail':useremail})

def furniture(request):
    login = request.session['login']
    useremail = request.session['email']
    data = UploadProductModel.objects.filter(category='furniture',status='Available')
    return render(request, 'products.html',{'login':login,'data':data,'useremail':useremail})

def shoes(request):
    login = request.session['login']
    useremail = request.session['email']
    data = UploadProductModel.objects.filter(category='shoes',status='Available')
    return render(request, 'products.html',{'login':login,'data':data,'useremail':useremail})

def electronics(request):
    login = request.session['login']
    useremail = request.session['email']
    data = UploadProductModel.objects.filter(category='electronics',status='Available')
    return render(request, 'products.html',{'login':login,'data':data,'useremail':useremail})

def clothing(request):
    useremail = request.session['email']
    login = request.session['login']
    data = UploadProductModel.objects.filter(category='clothing',status='Available')
    print(data,'=========')
    return render(request, 'products.html',{'login':login,'data':data,'useremail':useremail})


def viewprofile(request,mail):
    login = request.session['login']
    email = request.session['email']
    data = UsersModel.objects.filter(email=mail)
    return render(request, 'profile.html',{'login':login,'data':data,'email':email})    






def chat(request,id, mail): 
    # ChatModel.objects.all().delete()
    login = request.session['login'] 
    email = request.session['email']
    
    if mail == 'None' :
        messages.info(request, "Please select a user to send message")
        return redirect('products')
    if request.method ==  "POST":
        
        chat = request.POST['message']
        time = timezone.now()
        chats = ChatModel.objects.create(
                    cid=id, 
                    chat =chat ,
                    email = email,
                    remail=mail,
                    timestamp =time
                )
        chats.save()
        
        return redirect('chat',id,mail)
    chats = ChatModel.objects.filter((Q(cid=id) & ((Q(email=email) & Q(remail=mail)) |  Q(remail=email) & Q(email=mail))))  
 
    # print(chats)
    # for i in chats:
    #     print(i.email)
    #     print(i.remail)
    #     print(i.chat)
    return render(request,'chat.html',{'login':login, 'mail': mail,'chats': chats, 'id':id})
   

def viewchats(request):
    login = request.session['login']
    email = request.session['email']
    chats = ChatModel.objects.filter(remail=email)
    return render(request,'viewchats.html',{'login':login,'chats':chats})


def getproduct(request,id):
    login = request.session['login']
    email = request.session['email']
    product = UploadProductModel.objects.get(id=id)
    
    data=CollectedProducts.objects.create(
        product_name=product.product_name, category=product.category, 
            product_desc=product.product_desc, product_img=product.product_img, 
            uploaderemail=product.uploaderemail, upload_time=product.upload_time,
            collectedemail=email
    )
    data.save()
    product.status='Not Available'
    product.save()
    return redirect('products')


def collectedproducts(request):
    login = request.session['login']
    email = request.session['email']
    products = CollectedProducts.objects.filter(collectedemail=email)
    return render(request,'collectedproducts.html',{'login':login,'data':products})


def viewusers(request):
    login = request.session['login']
    # email = request.session['email']
    users = UsersModel.objects.all()
    return render(request,'viewusers.html',{'login':login,'data':users})


def acceptusers(request,id):
    login = request.session['login']
    data=UsersModel.objects.filter(id=id)
    data.update(status='Accepted')
    messages.success(request, ' Accepted Successfully')
    return redirect('viewusers')

def producttransactions(request):
    login = request.session['login']    
    data = CollectedProducts.objects.all()
    return render(request,'producttransactions.html',{'login':login,'data':data})