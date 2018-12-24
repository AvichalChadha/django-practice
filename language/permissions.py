from rest_framework import permissions
#The permission module contains all the base permission classes. 


class UpdateOwnProfile(permissions.BasePermission):
	"""Allow users to edit their own profile."""

	#There is a function inside the permission class called has_object permission. This function is called every time a request is made to our API. The result of that function determines weather the user have or doesn't have the permission to make the changes. 
	#This has_object permission function returns true or false depending upon what the result of the permission is. 
	def has_object_permission(self, request, view, obj):
		''' Check user is trying to edit their own profile. '''
		#A safe methid is a HTTP method that is classified as safe i.e it is a non destructive method. 
		#It allows us to retrieve data but it doesn't allow is to chanage or modify or delete any objects in the system. Basically GET method. 
		#Request object include the type of request that is made i.e get, post, put, del. 
		if request.method in permissions.SAFE_METHODS:
			return True
		else: 
			#This checks if the object the user is trying to change has the same id of the user who is currently authenticated.  
			return obj.id == request.user.id


