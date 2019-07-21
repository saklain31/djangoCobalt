from rolepermissions.roles import AbstractUserRole
from guardian.shortcuts import assign_perm
from django.shortcuts import render
from rolepermissions.roles import assign_role
from rolepermissions.checkers import has_permission

class Superuser(AbstractUserRole):
    available_permissions = {
        'is_superuser': True,
        'is_admin' : True,
        'is_manager' : True,
        'is_user' : True,
    }

class Admin(AbstractUserRole):
    available_permissions = {
        'is_admin' : True,
        'is_manager' : True,
        'is_user' : True,
    }

class Manager(AbstractUserRole):
	available_permissions = {
	    'is_manager' : True,
	    'is_user' : True,
	}


class User(AbstractUserRole):
	available_permissions = {
	    'is_user' : True,
	}


def set_object_permission(objperm,user,obj):
	assign_perm(objperm, user, obj)

def check_object_permission(objperm,user,obj):
	return user.has_perm(objperm,obj)

def set_role(user,perm):
	assign_role(user,perm)

def check_all_permission(user):
	print(user,'is superuser:',has_permission(user,'is_superuser'))
	print(user,'is admin:',has_permission(user,'is_admin'))
	print(user,'is manager:',has_permission(user,'is_manager'))
	print(user,'is user:',has_permission(user,'is_user'))

def check_permission(user,perm):
	return has_permission(user,perm)