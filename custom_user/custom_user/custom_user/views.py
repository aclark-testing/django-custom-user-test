from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.shortcuts import render


# Create your views here.


@login_required
def home(request):
    """
    """
    return render(request, 'home.html')


def signin(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # Redirect to a success page.
                return redirect('/')
            else:
                # Return a 'disabled account' error message
                pass
        else:
            # Return an 'invalid login' error message.
            pass
    return render(request, 'signin.html')


def signout(request):
    logout(request)
    return redirect('/')
