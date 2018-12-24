from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager  


class UserProfileManager(BaseUserManager):
	#creates a new user with this custom user model
	def create_user(self, email, name, password=None):
		if not email: 
			raise ValueError("enter the email dude!")
		email = self.normalize(email=email) #Put the email in lowercase.
		user = self.model(email=email, name = name) #In email=email, first email refers to the email in  UserProfile class and the second one refers to the normalized email
		#set_password will encrypt the password. 
		user.set_password(password)
		user.save(using=self.db)
		return user


		#creates and save a new superuser. 
	def create_superuser(self, email, name, password):
		user = self.create_user(email, name, password)
		user.is_superuser = True 
		user.is_staff = True 
		user.save(using=self.db)
		return user



#We are overwiting the django standard user model and creating our own. 
class UserProfile(AbstractBaseUser, PermissionsMixin):

	email = models.EmailField(max_length=255, unique=True)
	name = models.CharField(max_length=255)
	is_active = models.BooleanField(default=True)
	is_staff =  models.BooleanField(default=False)

	#An object manager is another class that we can use to manage the user Profiles. 
	#It gives us extra functionality like creating an adminstative user or regular user. 
	#AND IT IS REQUIRED WHEN WE SUBSTITUTE THE STANDARD UDER MODEL. 
	objects = UserProfileManager()

	USERNAME_FIELD = 'email'  #it is gonna be used as a username for this user. The standard django user model has something called the 'USERNAEM_FIELD'. It is used as the handle which is used to login the user. 
	REQUIRED_FIELDS = ['name'] #We are not writing the email because it is allready required in the above line.


	#used to get user full name. It is required to used our custom userProfile wich the DJANGO ADMIN
	def get_full_name(self):
		return self.name 


	def get_short_name(self):
		return self.name

	def __str__(self):
		return  self.email







class Paradigm(models.Model):
	name = models.CharField(max_length=50)
	def __str__(self):
		return self.name 


class programmingLang(models.Model):
	name = models.CharField(max_length = 50)
	paradigm = models.ForeignKey(Paradigm, on_delete = models.CASCADE)

	def __str__(self):
		return self.name 



class Programmer(models.Model):
	name = models.CharField(max_length=50)
	languages = models.ManyToManyField(programmingLang) 

	def __str__(self):
		return self.name