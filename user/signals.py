#signals importing
from allauth.account.signals import user_logged_in
from allauth.account.signals import user_logged_out
from allauth.account.signals import user_signed_up

#receiver importing
from django.dispatch import receiver

#model importing
from django.contrib.auth.models import User
from allauth.socialaccount.models import SocialAccount
from  . models import userProfile

#role file import
from djauth.roles import *

@receiver(user_logged_in)
def SaveLoggedinStatus(request,user,**kwargs):
	print("Someone logged in")
	try:
		#solution according to : https://docs.djangoproject.com/en/2.2/ref/contrib/auth/
		print(user)
		print(type(user))
		print(user.username)
		print(user.email)
		try:
			variable = userProfile.objects.get(userEmail=user.email)
			check_all_permission(user)
			if(len(variable)==0):
				social_info = SocialAccount.objects.get(user=request.user)
				uid=social_info.uid
				provider=social_info.provider
				first_name=user.first_name
				last_name=user.last_name
				email=user.email
				username=user.username

				newObject = userProfile()
				newObject.userFirstName = first_name
				newObject.userLastName = last_name
				newObject.userEmail = email
				newObject.username = username
				newObject.socialApplicationUid = uid
				newObject.save()
				print("First Time userProfile created")
		except Exception as e:
			print(e)
			try:
				social_info = SocialAccount.objects.get(user=request.user)
				uid=social_info.uid
				provider=social_info.provider
			except Exception as e:
				print(e)
				uid=""
				provider=""

			first_name=user.first_name
			last_name=user.last_name
			email=user.email
			username=user.username

			newObject = userProfile()
			newObject.userFirstName = first_name
			newObject.userLastName = last_name
			newObject.userEmail = email
			newObject.username = username
			newObject.userSerialNo= user.id
			newObject.userRole='user'
			if(uid != ""):
				newObject.socialAccountTableUid=uid
				newObject.provider=provider
				newObject.userTableName=''
			else:
				newObject.userTableName='userProfile'

			newObject.save()
			print("First Time userProfile created")

			#setting role
			try:
				print("Setting Role")
				set_role(user,'user')
				check_all_permission(user)
			except Exception as e:
				print(e)


	except Exception as e:
		print(e)
		pass
	return


@receiver(user_logged_out)
def SaveLoggedoutStatus(request,user,**kwargs):
	print(request.user)
	print("Someone Logged Out")
	return


@receiver(user_signed_up)
def SaveUserSignInformations(request,user,**kwargs):
	print("Someone signed in for the first time")
	return
