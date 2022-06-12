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

                        Welcome to Awwards

                        Thank you for signing up. 
                        We are excited to welcome you to the family.

                        Happy Posting.
                        Awwards Family
                        
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

def profile(request,id):
    user_profile = Profile.objects.get(id=id)
    user_projects = Project.objects.filter(owner=id)

    context={
        'user_profile':user_profile,
        'user_projects':user_projects
    }
    return render(request,'profile.html',context=context)

@login_required(login_url='login')
def profile_update(request,username):
    user_name = User.objects.get(username=username)
    user_profile = Profile.objects.get(user=user_name.id)

    data = get_object_or_404(Profile, id=user_profile.id)
    profile_form = ProfileUpdateForm(instance=data)

    if request.method == "POST":
        profile_form = ProfileUpdateForm(request.POST,request.FILES, instance=data)
        if profile_form.is_valid():
            profile_form.save()
            
            return redirect ('profile_update', username=user_name)

    context={
        'user_name':user_name,
        'profile_form':profile_form,
        'user_profile':user_profile
    }
    return render(request,'profile_update.html',context=context)

def homepage(request):
    all_projects = Project.objects.all()

    context={
        'all_projects':all_projects
    }
    return render(request,'index.html',context=context)

def project_details(request,id):
    project = Project.objects.get(id=id)
    user = Profile.objects.get(id=project.owner.id)

    context={
        'project':project,
        'user':user
    }
    return render(request,'project-details.html',context=context)

@login_required(login_url='login')
def create_project(request):
    project_form = ProjectUploadForm()

    context={
        'project_form':project_form
    }
    return render(request,'project-upload-form.html',context=context)

@login_required(login_url='login')
def like_project(request,user_id,project_id):
    profile_vote=Profile.objects.get(id=user_id)
    post_voted = Project.objects.get(id=project_id)

    new_like = PostVote(
        profile_vote=profile_vote,
        post_voted=post_voted
    )
    new_like.save_like()

    return redirect('homepage')