from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import FlatOwner, AddFlat, UserModel
from django.contrib.auth import authenticate, login, logout

# HOME PAGE FUNCTION
def Home(request):
    flat_data = AddFlat.objects.all()
    context = {'flat_data':flat_data}

    return render(request, 'Home.html', context)


# OWNER SIGNUP PAGE FUNCTION
def OwnerSignup(request):
    error = ''
    if request.method == 'POST':
        f = request.POST['fname']
        l = request.POST['lname']
        i = request.FILES['image']
        p = request.POST['pwd']
        e = request.POST['email']
        con = request.POST['contact']
        cp = request.POST['cpwd']

        user = User.objects.filter(username = e) 
        if user.exists():
            error = "Email Exist"

        elif p == cp:
            try:
                user = User.objects.create_user(first_name=f, last_name=l, username=e, password=p)
                FlatOwner.objects.create(user=user, mobile=con, image=i, type='Owner', status="Pending")
                error="no"
            except:
                error="yes"
        else:
            error = "yes"

    d = {'error':error}
    return render(request, 'OwnerSignup.html', d)


# OWNER LOGIN PAGE FUNCTION
def OwnerLogin(request):
    error = ""
    if request.method == 'POST':
        e = request.POST['email']
        p = request.POST['pwd']

        user = authenticate(username=e, password=p)
        
        if user:
            user1 = FlatOwner.objects.get(user=user)
            if user1.type == "Owner" and user1.status != "Pending":
                login(request, user) 
                error = "no"
            else:
                error = "not"
        else:
            error = "yes"
            
    d = {'error':error}
    return render(request, 'OwnerLogin.html', d)


# OWNER LOGOUT FUNCTION
def Logout(request):
    if not request.user.is_authenticated:
        return redirect("ownerlogin")
    
    logout(request)
    return redirect('/')


# ADD FLATS
def Add_Flat(request):
    if not request.user.is_authenticated:
        return redirect("ownerlogin")
    
    error = ""
    if request.method == 'POST':
        add = request.POST['address']
        cont = request.POST['contact']
        price = request.POST['price']
        ftype = request.POST['choice']
        img = request.FILES['image']
        c = request.POST['city']
        des = request.POST['desc']

        user = request.user
        owner = FlatOwner.objects.get(user=user)

        try:
            AddFlat.objects.create(owner=owner, address=add, contact=cont, price=price, flat_type=ftype, image=img, city=c, desc=des) 
            error = "no" 
        except: 
            error = "yes" 

    d = {'error': error} 
    return render(request, 'AddFlats.html', d) 


# OWNER DASHBOARD
def OwnerDashBoard(request):
    if not request.user.is_authenticated:
        return redirect("ownerlogin")
    
    user = request.user
    owner = FlatOwner.objects.get(user=user)
    data = AddFlat.objects.filter(owner=owner)
    d = {'data':data}
    return render(request, "OwnerDashboard.html",d)


# DELETE ADDED FLAT
def DeleteFlat(request, pid):
    if not request.user.is_authenticated:
        return redirect("ownerlogin")
    flat = AddFlat.objects.get(id=pid)
    flat.delete()
    return redirect('/ownerdashboard')


# EDIT OWNER FLAT
def EditFlat(request, pid):
    if not request.user.is_authenticated:
        return redirect("ownerlogin")
    
    ID = AddFlat.objects.get(id=pid)
    error = ""
    if request.method == 'POST':
        add = request.POST['address']
        cont = request.POST['contact']
        price = request.POST['price']
        ftype = request.POST['choice']
        img = request.FILES['image']
        c = request.POST['city']
        des = request.POST['desc']

        try:
            ID.address = add
            ID.contact = cont
            ID.price = price
            ID.flat_type = ftype
            ID.desc = des
            ID.city = c
            ID.image = img
            ID.save()
            error = "no"
        except:
            error = "yes"        
            
    d = {'ID':ID, 'error':error}
    return render(request, 'EditFlat.html', d)


# VIEW FLAT FUNCTION
def ViewFlat(request, pid):
    if not request.user.is_authenticated:
        return redirect('userlogin')
    ID = AddFlat.objects.get(id=pid)
    d = {'ID':ID}
    return render(request, 'ViewFlat.html', d)


# USER SIGNUP FUNCTION
def UserSignup(request):
    error = ""
    if request.method == 'POST':
        f = request.POST['fname']
        l = request.POST['lname']
        i = request.FILES['image']
        p = request.POST['pwd']
        e = request.POST['email']
        con = request.POST['contact']
        cp = request.POST['cpwd']

        user1 = User.objects.filter(username=e)
        if user1.exists():
            error = "Email Exist"
        
        elif p == cp:
            try:
                user = User.objects.create_user(first_name=f, last_name=l, username=e, password=p)
                UserModel.objects.create(user=user, mobile=con, image=i, type='user', status="Accept")
                error = "no"
            except:
                error = "yes"
        else:
            error = "yes"

    d = {'error':error}
    return render(request, 'UserPages/UserSignup.html', d)


# USER LOGIN FUNCTION
def UserLogin(request):
    error = ""
    if request.method == 'POST':
        e = request.POST['email']
        p = request.POST['pwd']

        user = authenticate(username=e, password=p)
        if user:
            user1 = UserModel.objects.get(user=user)
            if user1.type == "user" and user1.status != "Pending":
                login(request, user)
                error = "no"
            else:
                error = "not"
        else:
            error = "yes"

    d = {'error': error}
    return render(request, 'UserPages/UserLogin.html', d)