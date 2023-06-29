from django.db import models
from autoslug import AutoSlugField
class Customer_information(models.Model):
    First_Name=models.CharField(max_length=15)
    CustomerType=models.CharField(max_length=30)
    Email=models.EmailField(max_length=50)
    Contact=models.CharField(max_length=12)
    message=models.TextField(max_length=500)

class display_video(models.Model):
    link_1=models.CharField(max_length=200,null=False)
    link_2=models.CharField(max_length=200,null=False)
    
class testimonials(models.Model):
    name_1=models.CharField(max_length=40,null=False)
    description_1=models.TextField(max_length=300,null=False)
    name_2=models.CharField(max_length=40,null=False)
    description_2=models.TextField(max_length=300,null=False)

class Customer_order(models.Model):
    Name=models.CharField(max_length=20,null=False)
    Shipping_Address=models.CharField(max_length=50,null=False)
    Pincode=models.CharField(max_length=6,null=False)
    Mobile_Number=models.CharField(max_length=10,null=False)
    Billing_to=models.CharField(max_length=40,null=False)
    Billing_Address=models.CharField(max_length=50,null=False)
    refcode=models.CharField(max_length=10,null=True)
    Product_Required=models.IntegerField()
    Price=models.IntegerField()

class ref_code(models.Model):
    Referral_Code=models.CharField(max_length=10, null=False)
    Amount_reduction=models.IntegerField(null=False,default="0")

class Product_Amount(models.Model):
    Product_Name=models.CharField(max_length=30,null=False)
    Product_Amount=models.IntegerField(default="0")
