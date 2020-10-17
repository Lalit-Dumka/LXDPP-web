from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group

def home(request):
    return render(request, 'home.html')
def portfolio(request):
    return render(request, 'portfolio.html')
def userLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        # print(f'\n user\n============================== \n{user}\n\n============================')
        if user is not None:
            login(request,user)
            messages.success(request,'Successfully Logged in :)')
            return HttpResponseRedirect('/blog')
        else:
            messages.warning(request,'Failed to authenticate !! Incorrect credentials... Please enter correct username and password..')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')
def userSignup(request):
    if request.method == 'POST':
        username = request.POST.get('usernameInput')
        email = request.POST.get('emailInput')
        password = request.POST.get('passwordInput')
        first_name = request.POST.get('firstNameInput')
        last_name = request.POST.get('lastNameInput')
        
        user = authenticate(request, username=username, password=password)
        
        if user is None:
            user = User.objects.create_user(username, email, password, first_name=first_name, last_name=last_name)
            group = Group.objects.get(name='Author')
            user.groups.add(group)
            print(f'\n group\n\n\n\n\n============================== \n{user.groups}\n\n============================\n\n\n\n\n\n\n\n')
            messages.success(request, 'Congrats... You are now an Author!! Now create some cool stuff in LXDPP...')
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request,'Successfully Logged in :)')
            return HttpResponseRedirect('/blog')
        else:
            messages.warning(request, f'Failed to register... Please use valid characters in username, or try another username `{username}` maybe already taken !!! so, please try again with another one.')
            
            return render(request, 'signup.html')

    else:
        return render(request, 'signup.html')
def userLogout(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, 'Successfully Logged-out ')
        return HttpResponseRedirect('/blog')
    else:
        return HttpResponseRedirect('/login')
 

