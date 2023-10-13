from django.shortcuts import render, redirect
from medray.models import Customer_information, display_video, testimonials, Customer_order, ref_code, Product_Amount


def home(request):
    return render(request, "home.html")


def lenplate(request):
    return render(request, "Lenthening Plate.html")


def lennail(request):
    return render(request, "Limb Lenthening.html")


def tranail(request):
    return render(request, "Transport nail.html")


def traplate(request):
    return render(request, "Transport Plate.html")


def diggeo(request):
    show = display_video.objects.all()
    testi = testimonials.objects.all()
    # print(show[1].link_1) refrence to compare admin data with your data
    dict = {
        "show": show,
        "testi": testi
    }
    return render(request, "digitageo.html", dict)


def about(request):
    return render(request, "aboutus.html")


def congratulation(request):
    return render(request, "congratulation.html")


def buynow(request):
    amu = Product_Amount.objects.all()
    f_amount = int(amu[0].Product_Amount)
    if request.method == "POST":
        ref = ref_code.objects.all()
        if request.POST.get("customer_name") == "" or request.POST["customer_name"].isdigit() == True:
            return render(request, "buynow.html", {"bname": True})
        elif len(request.POST.get("pincode")) > 6 or len(request.POST.get("pincode")) < 6:
            return render(request, "buynow.html", {"pincode": True})
        elif len(request.POST.get("phonenumber")) > 10 or len(request.POST.get("phonenumber")) < 10 or request.POST["phonenumber"].isdigit() == False:
            return render(request, "buynow.html", {"phone": True})
        elif request.POST.get("quantity") == "0":
            return render(request, "buynow.html", {"quant": True})
        bname = request.POST.get("customer_name")
        shipping_address = request.POST.get("shipping_address")
        pincode = request.POST.get("pincode")
        phonenumber = request.POST.get("phonenumber")
        billto = request.POST.get("billto")
        billaddress = request.POST.get("billaddress")
        quantity = request.POST.get("quantity")
        Price = f_amount * int(quantity)
        refcode = request.POST.get("refcode")
        for i in range(len(ref)):
            if ref[i].Referral_Code == refcode:
                Price = Price-(int(ref[i].Amount_reduction)*int(quantity))
                break
        dicti = {
            "f_amount": f_amount,
            "bbname": bname,
            "shipping": shipping_address,
            "pincodee": pincode,
            "phonenumber": phonenumber,
            "billto": billto,
            "billadd": billaddress,
            "quantity": quantity,
            "refcode": refcode
        }
        if bname == "" or bname.isdigit() == True:
            dicti["bname"] = True
            return render(request, "buynow.html", dicti)
        elif len(pincode) > 6 or len(pincode) < 6:
            dicti["pincode"] = True
            return render(request, "buynow.html", dicti)
        elif len(phonenumber) > 10 or len(phonenumber) < 10 or phonenumber.isdigit() == False:
            dicti["phone"] = True
            return render(request, "buynow.html", dicti)
        elif quantity == "0":
            dicti["quant"] = True
            return render(request, "buynow.html", dicti)
        else:
            all_data = Customer_order(Name=bname, Shipping_Address=shipping_address, Pincode=pincode,
                                      Mobile_Number=phonenumber, Billing_to=billto, Billing_Address=billaddress, refcode=refcode, Product_Required=quantity, Price=Price)
            all_data.save()
            return redirect("/application-received/")
    return render(request, "buynow.html", {"f_amount": f_amount})


def signin(request):
    if request.method == "POST":
        email_var = False
        if request.POST["Email"].__contains__("@"):
            email_var = True
        if request.POST["Email"].__contains__(" "):
            email_var = False
        if request.POST["First name"] == "" or request.POST["First name"].isdigit() == True or request.POST["Email"] == "" or request.POST["Contact"] == "":
            return render(request, 'sign-in.html', {"error": True})
        elif email_var == False:
            return render(request, 'sign-in.html', {"error2": True})
        elif request.POST["docpat"] == "Please Select":
            return render(request, 'sign-in.html', {"error3": True})
        elif len(request.POST.get("Contact")) > 10 or len(request.POST.get("Contact")) < 10:
            return render(request, 'sign-in.html', {"error4": True})
        Fname = request.POST.get("First name")
        Customer = request.POST.get("docpat")
        Email = request.POST.get("Email")
        Contact = request.POST.get("Contact")
        Message = request.POST.get("Message")
        reg = Customer_information(First_Name=Fname, CustomerType=Customer,
                                   Email=Email, Contact=Contact, message=Message)
        reg.save()
        return render(request, 'sign-in.html', {"success": True})
    return render(request, 'sign-in.html')
