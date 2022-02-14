from django.shortcuts import render
from . models import *
from django.core.files.storage import FileSystemStorage
from random import random
from django.http.response import JsonResponse
# Create your views here.


def fnlogin(request):
    try:
        if request.method == 'POST':
            username = request.POST['email']
            print(username)
            password = request.POST['password']
            print(password)
            logi_obj = adminLogin.objects.get(
                username=username, password=password)
            request.session['log'] = logi_obj.id

            return render(request, 'dashboard.html')
    except Exception as e:
        print(e)
    return render(request, 'adminlogin.html')


def dashboard(request):
    return render(request, 'dashboard.html')


def fncustomer(request):
    return render(request, 'newcustomer.html')


def fnuser(request):
    try:
        if request.method == 'POST':
            name = request.POST.get('name')
            print(name)
            email = request.POST.get('email')
            print(email)
            password = request.POST.get('password')
            print(password)
            gender = request.POST.get('gender')
            print(gender)
            fathersname = request.POST.get('fname')
            print(fathersname)
            address = request.POST.get('address')
            print(address)
            city = request.POST.get('city')
            print(city)
            state = request.POST.get('state')
            print(state)
            country = request.POST.get('country')
            print(country)
            pincode = request.POST.get('pincode')
            print(pincode)
            mobile = request.POST.get('mobile')
            print(mobile)
            dob = request.POST.get('dob')
            print(dob)
            idproof = request.FILES.get('idproof')
            idproof_name = str(random())+idproof.name
            print(idproof_name)
            resume_obj = FileSystemStorage()
            resume_obj.save(idproof_name, idproof)
            photo = request.FILES.get('photo')
            photo_name = str(random())+photo.name
            print(photo_name)
            photo_obj = FileSystemStorage()
            photo_obj.save(photo_name, photo)
            customer_obj = customer(customername=name, gender=gender, fathername=fathersname, address=address, city=city, mobile=mobile,
                                    state=state, country=country, pincode=pincode, dob=dob, photo=photo_name, idproof=idproof_name)
            customer_obj.save()
            user_obj = user(email=email, password=password,
                            user_id_id=customer_obj.id)
            user_obj.save()
            return JsonResponse({'msg': 'Data added successfully'})
    except Exception as e:
        print(e)
    return render(request, 'newcustomer.html')


def fnnewloan(request):
    return render(request, 'newloan.html')


def fnitems(request):
    try:
        if request.method == 'POST':
            itemname = request.POST['item']
            print(itemname)
            item_obj = item(itemname=itemname)
            item_obj.save()
            return JsonResponse({'msg': 'Data added successfully'})
    except Exception as e:
        print(e)
    return render(request, 'items.html')


def fnitemgroup(request):
    try:
        if request.method == 'POST':
            igroup = request.POST['igroup']
            print(igroup)
            itemgroup_obj = itemtype(itemtype=igroup)
            itemgroup_obj.save()
            return JsonResponse({'msg': 'Data added successfully'})
    except Exception as e:
        print(e)
    return render(request, 'itemgroup.html')


def fninterest(request):
    try:
        if request.method == 'POST':
            intype = request.POST['intype']
            print(intype)
            iterest_obj = interest(interesttype=intype)
            iterest_obj.save()
            return JsonResponse({'msg': 'Data added successfully'})
    except Exception as e:
        print(e)
    return render(request, 'interesttype.html')


def loanhistory(request):
    return render(request, 'loanhistory.html')
