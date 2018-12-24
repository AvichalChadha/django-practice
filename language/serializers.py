from rest_framework import serializers
from . import models

class HelloSerializer(serializers.Serializer):
	#this is the validation that we get with serializer. In this case we the name shouldn't be more than 10 charecters. 
	name = serializers.CharField(max_length=10)
	age = serializers.CharField(max_length=10)



class UserProfileSerializer(serializers.ModelSerializer):
	class Meta: 
		model = models.UserProfile
		fields = ('id', 'email', 'name', 'password') #tupil
		extra_kwargs = {'password':{'write_only': True}} #Which specific fields we want to add keywords argument to. 
		#write only means we will never be able to see this through the serelizer. We can only write it. 
	
	#This is a special function that overwrites the create functionality. Reason for this is 
	#that we want to assign passwords correctly. This way we can store the password as a hash. 
	def create(self, validate_data): 
		user = models.UserProfile(
			email = validate_data['email'],
			name = validate_data['name']
		)

		user.set_password(validate_data['password'])
		user.save()

		return user


#this is a modelSerializer used along with the APIView.   /home/avichal/Downloads/Build a Backend REST API with Python & Django (lesson 30)
class ExampleSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.UserProfile
		fields = ('id', 'email', 'name')












class LanguageSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.programmingLang
		fields = ('id', 'name', 'paradigm')


class ParadigmSerializer(serializers.ModelSerializer):
	class Meta: 
		model = models.Paradigm
		fields = ('id', 'name')

class ProgrammerSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Programmer
		fields = ('id', 'name', 'languages')




