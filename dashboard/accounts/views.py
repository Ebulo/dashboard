from django.shortcuts import render, redirect
from django.contrib.auth.models import auth, User
from .models import Merchant_Details
from django.http import HttpResponse


def account(request):
    return render(request, "account.html")

def login(request):

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            print("log in Success.")
            return render(request, "customers.html")
        else:
            print("User is none.")
            return redirect("/account")
# Here we need to see if the user is a mercahnt or a normal user
"""
If user is a normal user then send him to the customers page'
else if the user is a merchant then send him to the client's page.
"""
    
    # return render(request, "registration.html")

def register(request):

     
    if request.method == "POST":
        name = request.POST['first_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                # username_err = messages.error(request, "username Taken")
                return render(request, 'account.html')
            elif  User.objects.filter(email=email).exists():
                # messages.error(request, "Email Taken")
                return render(request, 'account.html')
            else:
                user = User.objects.create_user(username=username, first_name=name, email=email, password=password1)
                user.save()

                # Login the user if successfully registered.
                log = auth.authenticate(username=username, password=password1)
                auth.login(request, log)
                # messages.info(request, "User Created Successfuly")
                return render(request, "customers.html")
        else:
            # messages.error(request, "Password not matching")
            return render(request, 'account.html')
    else:
        return render(request, 'account.html')


    # return HttpResponse("Registered!")
    # return render(request, "registration.html")

def merchant_register(request):
     
    if request.method == "POST":
        name = request.POST['first_name']
        username = request.POST['username']
        email = request.POST['email']
        
        is_merchant = True
        phone = request.POST['phone']
        adhar = request.POST['adhar']
        gstin = request.POST['gstin']
        bank = request.POST['bank']
        acc_name = request.POST['acc_name']
        ifsc = request.POST['ifsc']

        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                # username_err = messages.error(request, "username Taken")
                return render(request, 'account.html')
            elif  User.objects.filter(email=email).exists():
                # messages.error(request, "Email Taken")
                return render(request, 'account.html')
            else:
                user = User.objects.create_user(username=username, first_name=name, email=email, password=password1)
                user.save()
                merchant = Merchant_Details(is_merchant=is_merchant, first_name=name, username=username, email=email, phone=phone, adhar=adhar, gstin=gstin, bank=bank, acc_name=acc_name, ifsc=ifsc)
                merchant.save()

                # Login the user if successfully registered.
                log = auth.authenticate(username=username, password=password1)
                auth.login(request, log)
                # messages.info(request, "User Created Successfuly")
                return render(request, "client.html")
        else:
            # messages.error(request, "Password not matching")
            return render(request, 'account.html')
    else:
        return render(request, 'account.html')
    # return render(request, "registration.html")