from django.shortcuts import render
from django.contrib.auth import logout as auth_logout

# Create your views here.
def ShowSignUpInPage(request):
	return render(request,'SignUpIn.html')


def logout_view(request):
    """Logs out user"""
    auth_logout(request)
    return render(request, 'SignUpIn.html')
