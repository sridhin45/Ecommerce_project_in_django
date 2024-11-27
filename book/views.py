from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from book.models import *
from django.contrib import messages
from django.core.paginator import Paginator
from customer.models import *


def add_category(request):
    cat_list=category_tb.objects.all()
    p=Paginator(cat_list,2)
    page_number=request.GET.get('page')
    page_obj=p.get_page(page_number) 
    return render(request,'admin/viewcategory.html',{'ca':page_obj})

def categoryadd(request):
    if request.method=='POST':
        name=request.POST['name']
        data=category_tb(categoryname=name)
        data.save()
        messages.success(request,'category added successfully')
        return redirect('add_category')
    return render(request,'admin/addcategory.html')

def edit_ca(request,id):
    obj=get_object_or_404(category_tb,id=id)
    if request.method=='POST':
        name=request.POST['name']
        obj.categoryname=name
        obj.save()
        return redirect('add_category')
    cat=category_tb.objects.filter(id=id)
    return render(request,'admin/addcategory.html',{'ca':cat})

def delete_ca(request,id):
    category_tb.objects.filter(id=id).delete()
    return redirect('add_category')

def covertype(request):
    data=covertype_tb.objects.all()
    p=Paginator(data,2)
    page_number=request.GET.get('page')
    page_obj=p.get_page(page_number)
    return render(request,'admin/covertype.html',{'ca':page_obj})

def add_cover(request):
    if request.method=='POST':
        name=request.POST['name']
        data=covertype_tb(covertype=name)
        data.save()
        messages.success(request,'covertype added')
        return redirect('covertype')
    return render(request,'admin/add_cover.html')

def edit_co(request,id):
    obj=get_object_or_404(covertype_tb,id=id)
    if request.method=='POST':
        name=request.POST['name']
        obj.covertype=name
        obj.save()
        return redirect('covertype')
    cov=covertype_tb.objects.filter(id=id) 
    return render(request,'admin/add_cover.html',{'co':cov})   

def delete_co(request,id):
    covertype_tb.objects.filter(id=id).delete()
    return redirect('covertype')

def product(request):
    product=product_tb.objects.all()
    return render(request,'admin/product.html',{'pro':product})

def add_product(request):
    if request.method=="POST":
        title=request.POST['title']
        isbn=request.POST['isbn']
        author=request.POST['author']
        dec=request.POST['description']
        list=request.POST['listprice']
        price=request.POST['price']
        price50=request.POST['price50']
        price100=request.POST['price100']
        cate=request.POST['category']
        cover=request.POST['cover']
        if len (request.FILES)>0:
            image=request.FILES['image']
        else:
            image="no image"
        data=product_tb(title=title,isbn=isbn,author=author,description=dec,listprice=list,price=price,
        price50=price50,price100=price100,categoryid_id=cate,covertypeid_id=cover,image=image)

        data.save()
        messages.info(request,'product added..')
    category=category_tb.objects.all()
    covertype=covertype_tb.objects.all()
    return render(request,'admin/add_product.html',{'ca':category,'co':covertype})

def edit_product(request,id):
    str=get_object_or_404(product_tb,id=id)
    if request.method=='POST':
        old=product_tb.objects.filter(id=id)
        oldimg=old[0].image
        title=request.POST['title']
        isbn=request.POST['isbn']
        author=request.POST['author']
        dec=request.POST['description']
        listp=request.POST['listprice']
        price=request.POST['price']
        price50=request.POST['price50']
        price100=request.POST['price100']
        cate=request.POST['category']
        cover=request.POST['cover']
        if len(request.FILES)>0:
            image=request.FILES['image']
        else:
            image=oldimg
        new=product_tb.objects.get(id=id)
        new.image=image
        new.save()
        old.update(title=title,isbn=isbn,author=author,description=dec,listprice=listp,price=price,
        price50=price50,price100=price100,categoryid_id=cate,covertypeid_id=cover)
        return redirect('product')
    pro=product_tb.objects.filter(id=id)
    category=category_tb.objects.all()
    covertype=covertype_tb.objects.all()
    return render(request,'admin/add_product.html',{'pr':pro,'ca':category,'co':covertype})

    
def delete_product(request,id):
    product_tb.objects.filter(id=id).delete()
    return redirect('product')


def manageorder(request):
    return render(request,'admin/manageorder.html')

def load_table(request):
    type=request.GET.get('type')

    if type == '1':
        data=order_tb.objects.filter(order_status='pending')
    elif type =='2':
        data=order_tb.objects.filter(paymentstatus='pending')
    elif type =='3':
        data=order_tb.objects.filter(paymentstatus='paid')
    elif type == '4':
        data=Order_tb.objects.filter(order_status="reject")
    else:
        data=order_tb.objects.all()
    return render(request,'admin/load_table.html',{'da':data})

def more_details(request,id):
    order=order_tb.objects.filter(id=id)
    item=order_item.objects.filter(orderid=id)
    return render(request,'admin/more_details.html',{'or':order,'it':item})

def cancel_order(request,order_id):
    order_tb.objects.filter(id=order_id).update(order_status='rejected')
    return redirect('manageorder')

def processing(request):
    id=request.GET.get('id')
    order=order_tb.objects.get(id=id)
    date=request.GET.get('date')
    order.shipping_date=date
    order.orderstatus="processing"
    order.save()
    return redirect('manageorder')

def ship_order(request):
    orderid=request.POST['id']
    carrier=request.POST['carrier']
    tracking=request.POST['tracking']
    order_tb.objects.filter(id=orderid).update(carrier=carrier,tracking=tracking,orderstatus="shipped")
    return redirect('manageorder')










        

    














    


