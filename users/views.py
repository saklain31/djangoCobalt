from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render,HttpResponse
from django.contrib.auth import authenticate, login
from django.urls import reverse

from .forms import CustomUserCreationForm
from .models import *
from djauth.roles import *


# from rolepermissions.permissions import register_object_checker
# from rolepermissions.roles import get_user_roles
# from rolepermissions.checkers import has_object_permission



class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


def setUserPermissions(request):

	idx = 28

	user = CustomUser.objects.get(id=idx)
	print("***",user)

	set_role(user,'admin')
	check_all_permission(user)
	return HttpResponse(str(user)+' '+str(idx))



def getuser(request):
	current_user = request.user
	print(current_user.id)
	# setUserPermissions()
	
	return render(request,'home.html')


def createObjectWithPermission(request):
	event = Event.objects.create(name='eventTest')

	idx = 28

	user = CustomUser.objects.get(id=idx)
	# print("***",user)
	# print(event)
	# print(Manager)

	set_object_permission('edit_ev', user, event)
	print("*#*#*#" ,check_object_permission('edit_ev',user,event))

	# # objperm = access_event(Manager,user,event)
	# print('objperm '+objperm)

	return HttpResponse("hi")