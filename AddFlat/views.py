from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import FlatOwner, AddFlat
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

        if p == cp:
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


# OWNER HOME PAGE FUNCTION
def OwnerHome(request):
    if not request.user.is_authenticated:
        return redirect('ownerlogin')
    
    return render(request, 'OwnerHome.html')


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
        des = request.POST['desc']

        user = request.user
        owner = FlatOwner.objects.get(user=user)

        print(add, cont, price, des)

        try:
            AddFlat.objects.create(owner=owner, address=add, contact=cont, price=price, flat_type=ftype, image=img, desc=des) 
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
    flat = AddFlat.objects.get(id=pid)
    flat.delete()
    return redirect('/ownerdashboard')

# VIEW FLAT FUNCTION
# def ViewFlat(request, pid):
#     return render(request, 'ViewFlat.html')