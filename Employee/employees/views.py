from django.http import HttpResponse
from django.shortcuts import render, redirect 
from .forms import NewUserForm
from django.contrib.auth import login, authenticate,logout 
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import login
from django.contrib import messages
from movies.forms import EmployeeForm  
from movies.models import Employee  
# Create your views here.  
def emp(request):  
    if request.method == "POST":  
        form = EmployeeForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = EmployeeForm()  
    return render(request,'index.html',{'form':form})  
def show(request):  
    employees = Employee.objects.all() 
    #if not request.user.is_authenticated:
    #   form = AuthenticationForm()
    #   return render(request=request, template_name="login.html", context={"login_form":form})

    #else:
    return render(request,"show.html",{'employees':employees})  
def edit(request, id):  
    employee = Employee.objects.get(id=id)  
    if not request.user.is_authenticated:
       form = AuthenticationForm()
       return render(request=request, template_name="login.html", context={"login_form":form})
    else: 
       return render(request,'edit.html', {'employee':employee})  
def update(request, id):  
    employee = Employee.objects.get(id=id)  
    form = EmployeeForm(request.POST, instance = employee)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'employee': employee})  
def destroy(request, id):  
    employee = Employee.objects.get(id=id)  
    if not request.user.is_authenticated:
       form = AuthenticationForm()
       return render(request=request, template_name="login.html", context={"login_form":form})
    else:
       employee.delete()  
       return redirect("/show")  

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("/login")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("/show")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("/login")