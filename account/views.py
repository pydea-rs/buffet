from django.shortcuts import render, redirect
from .forms import RegisterForm
from .models import Account
from django.contrib import auth, messages


def auth_page(request):
    # this is when account first comes to log in/register page
    # create empty register and login form
    register_form = RegisterForm()

    # send data provided here to the template to show
    context = {
        'register_form': register_form,
    }
    return render(request, 'auth.html', context)  # render auth template


def register(request):
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():  # if everything entered as data is valid
            # and there is no account like this registered before
            username = register_form.cleaned_data['username']
            contact = register_form.cleaned_data['contact']
            password = register_form.cleaned_data['password']
            # create and register new account
            new_user = Account.objects.create_user(username=username, password=password, contact=contact)
            new_user.save()

            # if register was successful then render home page again
            # account can log in after that
            return redirect('home')
    else:
        register_form = RegisterForm()  # if method is not post, create an empty register form again

    # if method was not post or something went wrong
    # reload forms as normal
    context = {
        'register_form': register_form,
        'show_register_tab': True  # this will cause the page open register tab as active in page reload
    }
    # when registration fails or counter errors
    return render(request, 'auth.html', context)


def login(request):
    if request.method == 'POST':
        # read fields sent by account log in form
        print(request.POST)
        contact = request.POST['contact']
        password = request.POST['password']
        # check if the data provided by account is valid
        user = auth.authenticate(contact=contact, password=password)

        if user is not None:
            auth.login(request=request, user=user)
            return render(request, 'home.html')
        else:
            messages.error(request=request, message="ایمیل/شماره تلفن یا رمزعبور اشتباه است")

    # if method was not post or something went wrong
    # reload forms as normal
    register_form = RegisterForm()  # load login form again
    context = {
        'register_form': register_form,
    }
    # when registration fails or counter errors
    return render(request, 'auth.html', context)


def logout(request):
    auth.logout(request)
    return redirect('home')
