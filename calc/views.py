from os import name
from django.core.checks import messages
from django.db.models.fields import EmailField
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse, request
from django.contrib.auth.models import User, auth 
from django.contrib import messages
from django.http import JsonResponse

# Create your views here.
def home(request):
    return render(request,'home.html')

def register(request):
    return render(request,'register.html') 

def blood_rgistration (request):
    return render(request,'blood_registration.html')


#----------------------------for register----------------------------#

def register(request):
    
    if request.method =='POST':
        first_name = str(request.POST['first_name']),
        last_name = str(request.POST['last_name']),
        username = str(request.POST['username']),
        email = str(request.POST['email']),
        password1 = str(request.POST['password1']),
        password2 = str(request.POST['password2']),
        
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username is already exists')
                print('Username is already exists')
                return redirect('register')     
                #return HttpResponse('username is already exists')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email is already exists')
                print('email is already exists')
                return redirect('register') 
                #return HttpResponse('email is already exists')
            else:
                user = User.objects.create_user(
                    username= str(username),
                    email= str(email),
                    password=str(password1),
                    first_name=str(first_name),
                    last_name=str(last_name))
                user.save()
                print('user created')                     
                return redirect('/')
        else:
            print('password is not matching')
            return redirect('register.html')
            

    else:
        return render(request,'register.html') 

#----=--=-=---=-=-=-----=-=-=- sign up----=---=---==---===----#

def signup(request): 
  if request.method =='POST':

    username = str(request.POST['username'])
    password = str(request.POST['password'])

    #user = auth.authenticate(username=str(username),password=str(password))
    if username==username and password==password:
       # auth.login(request, user)
       # return redirect('display')
        return JsonResponse(
                {'success':True},
                safe=False
       )
    else:
        print('invalid credential')
        #messages.info(request,'Invalid credentials')
        #return redirect('/')
        return JsonResponse(
            {'success':False},
            safe=False
        )
  else:
      return render(request,'/')


#----------------------------registration form for blood donation---------

datas=[]
def add (request):

     if request.method =='POST':
        full_name = str(request.POST['full_name']),
        age = str(request.POST['age']),
        blood = str(request.POST['blood']),
        phone_no = str(request.POST['phone_no']),
        gender = str(request.POST['gender']),
        list= {
             'full_name':full_name,
             'age':age,
             'blood':blood,
             'phone_no':phone_no,
             'gender':gender
         }     
        datas.append(list)
        return redirect(display)
     else:
      return render(request,'blood_registration')
def display (request):
   context = {'datas':datas}
   return render(request,'result.html', context) 

def logout (request):
    auth.logout(request)
    return redirect('/')