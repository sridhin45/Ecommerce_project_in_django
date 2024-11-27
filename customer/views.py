from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from book.models import *
from django.contrib import messages
from . models import *
import datetime
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.urls import reverse
import stripe
from django.views.generic import TemplateView




def customerhome(request):
    product=product_tb.objects.all()
    return render(request,'customer/customerhome.html',{'pr':product})

def details(request,id):
    pro=product_tb.objects.filter(id=id)
    return render(request,'customer/details.html',{'pr':pro})

def add_cart(request):
    id=request.POST['id']
    userid=request.session['id']
    count=int(request.POST['count'])
    pro=product_tb.objects.filter(id=id)

    if cart_tb.objects.filter(userid=userid,productid=id):
        cart=cart_tb.objects.get(userid=userid,productid=id)
        cart.count+=count
        if cart.count<50:
            cart.price=pro[0].price
        elif cart.count<100:
            cart.price=pro[0].price50
        else:
            cart.price=pro[0].price100
        cart.save()
    else:
        if count<50:
            price=pro[0].price
        elif count<100:
            price=pro[0].price50
        else:
            price=pro[0].price100
        
        data=cart_tb(userid_id=userid,productid_id=id,count=count,price=price)
        data.save()
    messages.info(request,'added to cart')
    product=product_tb.objects.all()
    return render(request,'customer/customerhome.html',{'pr':product})

def cartview(request):
    grandtotal=0
    cart=cart_tb.objects.filter(userid=request.session['id'])
    for c in cart:
        totle=c.count*c.price
        grandtotal+=totle
    return render(request,'customer/cartview.html',{'ca':cart,'gr':grandtotal})

def plus(request,id):
    cart=cart_tb.objects.get(id=id)
    cart.count=cart.count+1
    if cart.count<50:
        cart.price=cart.productid.price
    elif cart.count<100:
        cart.price=cart.productid.price50
    else:
        cart.price=cart.productid.price100
    cart.save()
    return redirect('cartview')

def minus(request,id):
    cart=cart_tb.objects.get(id=id)
    cart.count=cart.count-1
    if cart.count<50:
        cart.price=cart.productid.price
    elif cart.count<100:
        cart.price=cart.productid.price50
    else:
        cart.price=cart.productid.price100
    cart.save()
    return redirect('cartview')

def delete_cart(request,id):
    cart_tb.objects.filter(id=id).delete()
    return redirect('cartview')

def summary(request):
    user=Customer_tb.objects.filter(id=request.session['id'])
    cart=cart_tb.objects.filter(userid=request.session['id'])
    grandtotal=request.GET.get('gr')
    return render(request,'customer/summary.html',{'us':user,'ca':cart,'gr':grandtotal})

def create_checkout_session(request):
    id=Customer_tb.objects.get(id=request.session['id'])
    email=id.Email
    grandtotal=request.POST['grandtotal']
    date=datetime.datetime.now()
    name=request.POST['name']
    phone=request.POST['phone']
    address=request.POST['address']
    city=request.POST['city']
    state=request.POST['state']
    code=request.POST['code']
    order=order_tb(userid_id=request.session['id'],name=name,phone=phone,address=address,city=city,state=state,
                   postel_code=code,email=email,order_date=date,order_total=grandtotal,transactionid=0)
    order.save()
    cart=cart_tb.objects.filter(userid=request.session['id'])

    for item in cart:
       pid=item.productid_id
       count=item.count
       total=item.price
       orderid=order.id
       orderlist=order_item(orderid_id=orderid,productid_id=pid,count=count,price=total)
       orderlist.save()


    domain_url='http://localhost:8000/'
    stripe.api_key=settings.STRIPE_SECRET_KEY




    customerid=request.session['id']
    cart_items=cart_tb.objects.filter(userid_id=customerid)
    line_items=[]
    for item in cart_items:
        line_items.append({
            'price_data':{
                'currency':'usd',
                'product_data' : {
                    'name':item.productid.title,
                },
                'unit_amount':item.price
            },
            'quantity':item.count
        })
    checkout_session=stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=line_items,
        mode='payment',
        success_url=request.build_absolute_uri(reverse('checkout_success'))+"?session_id={CHECKOUT_SESSION_ID}",   #or domain_url+'success/'
        cancel_url=request.build_absolute_uri(reverse('checkout_cancel')),
        metadata={'order_id': order.id}  # Attach order ID to metadata
    )
    return redirect(checkout_session.url)

class successview(TemplateView):
    template_name='success.html'
    def get(self, request, *args, **kwargs):
        session_id = request.GET.get("session_id")

        if not session_id:
            return HttpResponse('session id missing',status=400)
        try:
            session = stripe.checkout.Session.retrieve(session_id)
            print(f"Session : {session}")


            if session.payment_status=='paid':
                order_id=session.metadata.get("order_id")


                order = get_object_or_404(order_tb, id=order_id)

                order.paymentstatus='paid'
                order.paymentduedate=datetime.date.today()
                order.transactionid=session_id
                order.save()
        except stripe.error.StripeError as e:
            return HttpResponse(f"Stripe error: {str(e)}", status=500)
        
        return super().get(request, *args, **kwargs)

class CancelView(TemplateView):
    template_name="cancel.html"















