from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views.generic.edit import CreateView 
from .forms import RegistrationForm, LoginForm, ProfileForm, PostForm, MessageForm
from .models import Profile, Post, Message
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

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

    if request.method == "POST":
        profile_form = ProfileForm(request.POST, request.FILES, instance=user_profile)

        if profile_form.is_valid():
            profile_form.save()
            return redirect('profile')
    
    else:
        profile_form = ProfileForm(instance=user_profile)
    
    return render(request, 'profile.html', {"profile_form": profile_form, "user_profile": user_profile, "user_posts": user_posts})

@login_required
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()

            return redirect('profile')
        
    else:
        form = PostForm()
    
    return render(request, 'create_post.html', {"form": form})


class SendMessageView(LoginRequiredMixin, CreateView):
    model = Message
    form_class = MessageForm
    template_name = 'send_message.html'
    success_url = "/profile/"

    def form_valid(self, form):
        form.instance.sender = self.request.user
        self.as_view

        return super().form_valid(form)
