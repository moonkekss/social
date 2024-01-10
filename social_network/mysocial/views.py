from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views.generic.edit import CreateView 
from .forms import RegistrationForm, LoginForm, ProfileForm, PostForm, MessageForm
from .models import Profile, Post, Message
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

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
    user_posts = Post.objects.filter(user=request.user)
    post_form = PostForm()  # Initialize your PostForm here

    if request.method == "POST":
        # Check if the POST request is for profile update
        if 'profile' in request.POST:
            profile_form = ProfileForm(request.POST, request.FILES, instance=user_profile)
            if profile_form.is_valid():
                profile_form.save()
                return redirect('profile')
        # Check if the POST request is for post creation
        elif 'post' in request.POST:
            post_form = PostForm(request.POST, request.FILES)
            if post_form.is_valid():
                post = post_form.save(commit=False)
                post.user = request.user
                post.save()
                if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                    return JsonResponse({'status': 'success'})
                return redirect('profile')
    else:
        profile_form = ProfileForm(instance=user_profile)

    context = {
        "profile_form": profile_form,
        "post_form": post_form,  # Pass 'post_form' to the template context
        "user_profile": user_profile,
        "user_posts": user_posts
    }
    return render(request, 'profile.html', context)

@login_required
def send_message(request):
    if request.method == "POST":
        form = MessageForm(request.POST )

        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.save()
            
            return redirect('profile')
        
    else:
        form = MessageForm()
    return render(request, 'send_message.html', {"form": form})

@login_required
def inbox(request):
    messages = Message.objects.filter(recevier=request.user).order_by("-date_sent")

    return render(request, 'inbox.html', {"messages": messages})

@login_required
def read_message(request, message_id):
    message = get_object_or_404(Message, id=message_id, receiver=request.user)
    message.is_read = True  
    message.save()

    return render(request, 'read_message.html', {"message": message})