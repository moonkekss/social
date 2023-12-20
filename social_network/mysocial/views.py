from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegistrationForm, LoginForm, ProfileForm, PostForm
from .models import Profile, Post
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user= form.save()
            login(request, user)
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request,request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})


@login_required
def home(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'home.html', {"posts": posts})

@login_required
def profile(request):
    user_profile = Profile.objects.get(user=request.user)

    if request.method == "POST":
        profile_form = ProfileForm(request.POST, request.FILES, instance=user_profile)

        if profile_form.is_valid():
            profile_form.save()
            return redirect('profile')
    
    else:
        profile_form = ProfileForm(instance=user_profile)
    
    return render(request, 'profile.html', {"profile_form": profile_form, "user_profile": user_profile})

@login_required
def create_post(request):
    if request.method == "POST":
        post_form = PostForm(request.POST)

        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.user = request.user
            post.save()

            return redirect('profile')
        
    else:
        post_form = PostForm()
    
    return render(request, 'create_post.html', {"post_form": post_form})
