from django.db import models

class admin_tb(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=20)

class category_tb(models.Model):
    categoryname=models.CharField(max_length=50)

class covertype_tb(models.Model):
    covertype=models.CharField(max_length=50)

class product_tb(models.Model):
    title=models.CharField(max_length=50)
    isbn=models.IntegerField()
    author=models.CharField(max_length=50)
    description=models.TextField()
    listprice=models.PositiveIntegerField()
    price=models.PositiveIntegerField()
    price50=models.PositiveIntegerField()
    price100=models.PositiveIntegerField()
    categoryid=models.ForeignKey(category_tb, on_delete=models.CASCADE)
    covertypeid=models.ForeignKey(covertype_tb, on_delete=models.CASCADE)
    image=models.FileField()











