from multiprocessing import context
from os import abort
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate , login as dj_login, logout 
from django.contrib.auth.models import User
from .models import *
from django.contrib import messages

# Create your views here.
def home(request):

    return render(request, 'DjangoApp/home.html')

# Admin access
def dashboard(request):
    if not request.user.is_authenticated:
        messages.error(request, 'You must log in')
        return redirect('login')

    # Admin access only
    customer=Customer.objects.get(user=request.user.id)
    if customer.is_admin==True:
        # calling Customer model to loop over how many users we got using count() function.
        users=Customer.objects.all().count()
        #same as above, however, we used a regular for loop to go over the leaveReport model.
        total_leaves=leaveReport.objects.all()
        new=0
        total=0 
        confirm=0
        for i in total_leaves:
            if i.leave_status=="pending":
                new+=1
            elif i.leave_status=="Accept":
                confirm+=1
            total+=1
    else:
        messages.warning(request, 'Not authorized')
        return redirect('user_profile')

    context={'new':new, 'confirm':confirm, 'total':total, 'users':users}
    return render(request, 'DjangoApp/dashboard.html',context)

####################################################################################### signUp, Login, Logout routes
def signUp(request):
    if request.method == "POST":
        name=request.POST['name']
        email=request.POST['email']
        pno=request.POST['pno']
        pwd1=request.POST['pwd1']

        try:
            user=User.objects.create_user(username=email, password=pwd1, first_name=name)
            Customer.objects.create(user=user, phone_no=pno)
            messages.success(request, 'User has been successfully registered')
            return redirect('login')
        except:
             messages.error(request, 'sth wrong happened, try again')
             return redirect('signup')
             
       
    context = {}
    return render(request, 'DjangoApp/signup.html',context)

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password =request.POST['pwd1']

        user = authenticate(username=email, password=password)
        try:
            if user:
                customer=Customer.objects.get(user=user)
                dj_login(request,user)
                # redirect to the appropriate page
                if customer.is_admin!=True:
                    messages.success(request, 'You have successfully logged in')
                    return redirect('user_profile')  
                elif customer.is_admin==True:
                    messages.success(request, 'You have successfully logged in')
                    return redirect('dashboard')
                else:
                    messages.error(request,'Sth wrong happened , try again')   
                    
            else:
                    messages.error(request, "Email or Password not correct.")   
        except:
             messages.error(request, 'User doesnot exist , try again')
             return redirect('login')
                    
    context={}
    return render(request, 'DjangoApp/login.html',context)

def logoutUser(request):
	logout(request)

	return redirect('login')


######################################################################################### Leaves routes 
def getLeave(request):
    if not request.user.is_authenticated:
        messages.error(request, 'You must log in')
        return redirect('login')

    return render(request, 'DjangoApp/apply_leave.html')

def addLeave(request):
    if request.method=="GET":
        # redirect to the getLeave function but I named it differently within urls.py
        return redirect('apply_leave')
    else:
    #1- creating variables to access the values that coming from the html POST
        leave_date=request.POST['leave_date']
        leave_msg=request.POST['leave_msg']
    # calling Customer model to get current user id (customer object) 
        customer=Customer.objects.get(user=request.user.id)
        try:
    #2- specifying the Object from the class "leave Report"
            leave_report=leaveReport(customer=customer, leave_date=leave_date, 
                                    leave_message=leave_msg, leave_reply='', leave_status="pending")
            leave_report.save()
            messages.success(request, 'Leave request has been successfully submitted')
            return redirect('all_leave')
        except:
            messages.error(request, 'sth wrong happened, try again')
            return redirect('all_leave')


#Admin access
def allLeave(request):
    if not request.user.is_authenticated:
        messages.error(request, 'You must log in')
        return redirect('login')

    # calling Customer model to get current user id (customer object) 
    customer=Customer.objects.get(user=request.user.id)
    # calling leaveReport model to get all issued leaves that belong to the customer(user)
    leave_report=leaveReport.objects.filter(customer=customer)

    context={'leave_report':leave_report}
    return render(request, 'DjangoApp/all_leave.html', context)


#Admin access
def newLeave(request):
    if not request.user.is_authenticated:
        messages.error(request, 'You must log in')
        return redirect('login')
    try:
        #1 calling Customer model to get current user id
        customer=Customer.objects.get(user=request.user.id)
         #2 Admin access only
        if customer.is_admin==True:
            #messages.warning(request, 'you successed')
            leave_report=leaveReport.objects.filter(leave_status="pending")
            context = {'leave_report':leave_report}
            return render(request, 'DjangoApp/new_leave.html', context)

        else:
            messages.warning(request, 'Not authorized')
            return redirect('user_profile')
    except:
        messages.error(request, 'sth wrong happened, try again')
        return redirect('user_profile')
#Admin access
def confirmLeave(request):
    if not request.user.is_authenticated:
        messages.error(request, 'You must log in')
        return redirect('login')
    try:
        #1 calling Customer model to get current user id
        customer=Customer.objects.get(user=request.user.id)
         #2 Admin access only
        if customer.is_admin==True:
            #messages.warning(request, 'you successed')
            leave_report=leaveReport.objects.filter(leave_status="Accept")
            context = {'leave_report':leave_report}
            return render(request, 'DjangoApp/confirm_leave.html', context)

        else:
            messages.warning(request, 'Not authorized')
            return redirect('user_profile')
    except:
        messages.error(request, 'sth wrong happened, try again')
        return redirect('user_profile')
#Admin access
def userFeedback(request,pd):
    if not request.user.is_authenticated:
        messages.error(request, 'You must log in')
        return redirect('login')

    #1 calling Customer model to get current user id
    customer=Customer.objects.get(user=request.user.id)
    #2 Admin access only
    if customer.is_admin==True:
    #3 calling leaveReport model to get current leave id
        leave_id=leaveReport.objects.get(id=pd)
        if request.method=="POST":
            get_status=request.POST['leave_status'] 
            get_feedback=request.POST['leave_feedback'] 
            leave_id.leave_status=get_status
            leave_id.leave_reply=get_feedback
            leave_id.save()
            messages.success(request, 'Action has been successfully submitted')
            return redirect('new_leave')
    else:
            messages.warning(request, 'Not authorized')
            return redirect('user_profile')
    context={'leave_id':leave_id}
    return render(request, 'DjangoApp/user_feedback.html',context)

######################################################################################### Users routes
# userprofile route
def userProfile(request):
    if not request.user.is_authenticated:
        messages.error(request, 'You must log in')
        return redirect('login')

    # user=User.objects.get(id=request.user.id)
    customer=Customer.objects.get(user=request.user.id)
    context = {'customer':customer}
    return render(request, 'DjangoApp/user_profile.html', context)


# get alluser, Admin access
def allUser(request):
    if not request.user.is_authenticated:
        messages.error(request, 'You must log in')
        return redirect('login')

    #1 calling Customer model to get current user id
    customer=Customer.objects.get(user=request.user.id)
    #2 Admin access only
    if customer.is_admin==True:
        users=Customer.objects.all()
    else:
        messages.warning(request, 'Not authorized')
        return redirect('user_profile')

    context = {'users':users}
    return render(request, 'DjangoApp/all_user.html',context)

# delete user, #Admin access 
def delUser(request, pd):
    if not request.user.is_authenticated:
        messages.error(request, 'You must log in')
        return redirect('login')

    # user=User.objects.get(id=request.user.id)
    customer=Customer.objects.get(user=pd)
    messages.success(request, 'User has been successfully deleted')
    customer.delete()

    return redirect('all_user') 
