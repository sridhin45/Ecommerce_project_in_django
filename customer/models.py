from django.db import models

# Create your models here.

class Customer_tb(models.Model):
    Name=models.CharField(max_length=20)
    Email=models.EmailField()
    Mobile=models.IntegerField()
    Address=models.CharField(max_length=20)
    City=models.CharField(max_length=20)
    State=models.CharField(max_length=20)
    Postal_code=models.CharField(max_length=20)
    username=models.CharField(max_length=50)
    Password=models.CharField(max_length=20)

class cart_tb(models.Model):
    userid=models.ForeignKey(Customer_tb,on_delete=models.CASCADE) 
    productid=models.ForeignKey('book.product_tb',on_delete=models.CASCADE)
    count=models.IntegerField()
    price=models.IntegerField()

class order_tb(models.Model):
    userid=models.ForeignKey(Customer_tb,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    phone=models.IntegerField()
    address=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    postel_code=models.CharField(max_length=50)
    email=models.EmailField(max_length=254)
    order_date=models.CharField(max_length=50)
    order_status=models.CharField(max_length=50,default='pending')
    order_total=models.IntegerField()
    carrier=models.CharField(max_length=50,blank=True)
    tracking=models.CharField(max_length=50,blank=True)
    shiping_date=models.CharField(max_length=50,blank=True)
    transactionid=models.CharField(max_length=50,blank=True)
    paymentduedate=models.CharField(max_length=50,blank=True)
    paymentstatus=models.CharField(max_length=50,default='pending')

class order_item(models.Model):
    orderid=models.ForeignKey(order_tb, on_delete=models.CASCADE)
    productid=models.ForeignKey('book.product_tb', on_delete=models.CASCADE)
    count=models.IntegerField()
    price=models.IntegerField()


    



