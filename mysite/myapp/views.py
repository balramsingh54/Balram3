from django.shortcuts import render,redirect
from myapp.forms import *
from django.contrib.auth.models import User
from myapp.models import *
from django.contrib import auth
# Create your views here.
def show(request):
	return render(request,'index.html')
	
def show1(request):
	return render(request,'top.html')
	
def show2(request):
	return render(request,'left.html')
	
def show3(request):
	return render(request,'bottom.html')
def reg(request):
	if request.method == "POST":  
		form = RegisterForm(request.POST)  
		if form.is_valid():  
			try:  
				form.save()  
				return redirect('/success')  
			except:  
				pass  
	else:  
		form = RegisterForm()  
	return render(request,'register.html',{'lalit':form})  

def login(request):
	if request.method=='POST':
		username = request.POST['userid']
		password = request.POST['passwd']
		print(password)
		user = auth.authenticate(Userid=username,Passwd=password)
		print(user)
		if user is not None:
			auth.login(request,user)
			return redirect('/valid')
		else:
			return redirect('/invalid')
	else:
		form=LoginForm()
	return render(request,'login.html',{'lalit':form})

def show4(request):
	return render(request,'success.html')
def show5(request):
	return render(request,'valid.html')
def show6(request):
	return render(request,'invalid.html')