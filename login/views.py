from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout #add this
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm #add this

# Create your views here.

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("/")
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form":form})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)  
        if form.is_valid():
            form.save()
            return redirect('/login/')
        else:
            print("ERROR")
    else:  
        form = UserCreationForm()  
    context = {  
        'form':form  
    }
    template = loader.get_template('register.html')
    return HttpResponse(template.render(context, request))


def logout(request):
    auth_logout(request)
    return redirect('/')