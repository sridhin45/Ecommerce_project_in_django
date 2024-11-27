from django.shortcuts import render,redirect
from book.models import *
from django.contrib import messages
from customer.models import *


def commonbase(request):
    return render(request,'common/commonbase.html')

def login(request):
    if 'id' in request.session:  
        if request.session.get('role') == 'admin':
            return render(request,'admin/adminhome.html')
        elif request.session.get('role') == 'customer':
           return redirect('customerhome')

    elif request.method == "POST":
        uname=request.POST['username']
        password=request.POST['password']
        admin=admin_tb.objects.filter(password=password,username=uname)
        customer=Customer_tb.objects.filter(username=uname,Password=password)

        if admin.count()>0:
            request.session['id']=admin[0].id
            request.session['admin']=admin[0].username
            request.session['role']='admin'
            messages.success(request,"login successfull as admin")
            return render(request,'admin/adminhome.html')
        elif customer.count()>0:
            request.session['id']= customer[0].id
            request.session['role']='customer'
            request.session['customerr']= customer[0].username  
            messages.success(request,"login successfull as user")  
            return redirect('customerhome')
        else:
            message.error(request,'invalid username or password')
            return render(request,'common/login.html')
    else:        
        return render(request,'common/login.html')

def adminhome(request):
    return render(request,'admin/adminhome.html')

def logout(request):
      request.session.flush()
      return redirect('login')


def register(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        mobile=request.POST['mobile']
        address=request.POST['address']
        city=request.POST['city']
        state=request.POST['state']
        code=request.POST['code']
        username=request.POST['username']
        password=request.POST['password']
        data=Customer_tb(Name=name,Email=email,Mobile=mobile,Address=address,City=city,State=state,Postal_code=code,username=username,Password=password)
        data.save()
    return render(request,'common/register.html')


def userlogout(request):
      request.session.flush()
      return redirect('login')
       






    
    


