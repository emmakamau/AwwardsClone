from multiprocessing import context
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .decorators import *
from .forms import *
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail,BadHeaderError

# Create your views here.
@unauthenticated_user
def signup(request):
    form = SignUpForm()

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')

            user_profile=Profile(
                user=user,
                name=username
            )
            user_profile.save_profile()

            subject = 'Welcome to IG'
            recipient_list = email
            message =   '''   
                        Hello,

                        Welcome to IG

                        Thank you for signing up. 
                        We are excited to welcome you to the family.

                        Happy Posting.
                        IG Family
                        
                        '''
            from_email = 'no-reply@example.com'
            try:
                send_mail(subject, message, from_email, [recipient_list])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')

            messages.success(request, "Account created successfully")
            return redirect('login')

    context = {
        'form': form,
    }
    return render (request, 'accounts/signup.html', context=context)

@unauthenticated_user
def loginuser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            messages.info(request, "Username or Password is incorrect")
            
    context = {}
    return render (request, 'accounts/login.html', context=context)

def logoutuser(request):

    logout(request)
    return redirect('login')

def homepage(request):
    

    context={
    }
    return render(request,'index.html',context=context)