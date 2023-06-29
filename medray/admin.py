from django.contrib import admin
from medray.models import Customer_information,display_video,testimonials,Customer_order,ref_code,Product_Amount

class userinformation(admin.ModelAdmin):
    list_display=("First_Name","CustomerType","Email","Contact","message")

class video_link(admin.ModelAdmin):
    list_display =("link_1","link_2")

class alumini(admin.ModelAdmin):
    list_display=("name_1","description_1","name_2","description_2")

class Product_BuyInfo(admin.ModelAdmin):
    list_display=("Name","Shipping_Address","Pincode","Mobile_Number","Billing_to","Billing_Address","refcode","Product_Required","Price")

class Referral(admin.ModelAdmin):
    list_display=("Referral_Code","Amount_reduction")

class Price(admin.ModelAdmin):
    list_display=("Product_Name","Product_Amount")

admin.site.register(Customer_information,userinformation)
admin.site.register(display_video,video_link)
admin.site.register(testimonials,alumini)
admin.site.register(Customer_order,Product_BuyInfo)
admin.site.register(ref_code,Referral)
admin.site.register(Product_Amount,Price)