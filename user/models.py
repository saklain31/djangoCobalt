from django.db import models

import uuid

# Create your models here.
class userProfile(models.Model):
	#basic ID
	userID = models.AutoField(primary_key=True)
	#personal information
	username = models.CharField(max_length=100,default="")
	userFirstName = models.CharField(max_length=30,default="")
	userLastName =  models.CharField(max_length=30,default="")
	userEmail = models.EmailField()
	userContact = models.CharField(max_length=20,default="")
	userAddress = models.CharField(max_length=30,default="")
	userCity = models.CharField(max_length=30,default="")
	userState = models.CharField(max_length=30,default="")
	userZipcode =  models.CharField(max_length=30,default="")
	userPassportID = models.CharField(max_length=30,default="")
	userNationalID = models.CharField(max_length=30,default="")

	#extra authetication stuffs
	socialAccountTableUid = models.TextField(blank=True, null=True)
	provider = models.CharField(default="",max_length=30)

	#user image
	userImage = models.ImageField(blank=True, upload_to='userImages', default='userImages/no-image.jpg')

	#Most important stuff to link
	userSerialNo=models.IntegerField(default=0) #this comes from user table in Django, the primary key in that table, the 'id' attribute
	userCode= models.UUIDField(default=uuid.uuid4,blank=True) #the UUID code which we will work with, will be shared into multiple table
	userRole=models.CharField(max_length=10,default="user") #the main role [user,admin,manager,superuser]
	userTableName=models.CharField(max_length=30,default="userProfile") #the meta data is kept into which table


	def __str__(self):
		return str(self.userID)
