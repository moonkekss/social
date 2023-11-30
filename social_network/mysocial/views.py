from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            print(f'Username: {username}, Password: {password}')
            user = authenticate(request, username=username, password=password)


            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                # Print form errors for debugging
                print(form.errors)

                form.add_error(None, "Invalid username or password")
        else:
            # Print form errors for debugging
            print(form.errors)
    else:
        form = UserLoginForm()

    return render(request, 'registration/login.html', {'form': form})


@login_required
def home(request):
    print(request.user.is_authenticated)
    # Эта функция представляет вашу главную страницу для зарегистрированных пользователей
    return render(request, 'home.html')
