from django.contrib import admin
from django.urls import path
from django.conf.urls import include


from . views import *

urlpatterns = [
	path('sign-up-in/',ShowSignUpInPage,name='ShowSignUpInPage'),
]