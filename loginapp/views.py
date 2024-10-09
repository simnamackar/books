from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import render, redirect

from . models import UserProfile,logintable

def userregistration(request):
    login_table=logintable()
    user_profile=UserProfile()

    if request.method=="POST":
        user_profile.username=request.POST['username']
        user_profile.firstname = request.POST['firstname']
        user_profile.lastname = request.POST['lastname']
        user_profile.email = request.POST['email']
        user_profile.password=request.POST['password']
        user_profile.password2= request.POST['password2']
        login_table.username=request.POST['username']
        login_table.password = request.POST['password']
        login_table.password2 = request.POST['password2']
        login_table.type='user'

        if request.POST['password']==request.POST['password2']:
            user_profile.save()
            login_table.save()
            messages.info(request,'registration successfull')
            return redirect('login')
        else:
            messages.info(request,'password not matching')
            return redirect('register')
    return render(request,'register.html')

def loginpage(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        # password2 = request.POST['password2']
        user=logintable.objects.filter(username=username,password=password,type='user').exists()
        try:
            if user is not None:
                user_details=logintable.objects.get(username=username,password=password)
                user_name=user_details.username
                type=user_details.type

                if type=='user':
                    request.session['username']=user_name
                    return redirect('viewbook')
                elif type=='admin':
                    request.session['username'] = user_name
                    return redirect('admin_view')
            else:
                messages.error(request,'invalid username or password')
        except:
            messages.error(request,'invalid role')
    return render(request,'login.html')

def admin_view(request):
    user_name=request.session['username']
    return render(request,'admin_view.html',{'user_name':user_name})
def user_view(request):
    user_name = request.session['username']
    return render(request,'user_view.html',{'user_name':user_name})

def logoutview(request):
    logout(request)
    return redirect('login')
