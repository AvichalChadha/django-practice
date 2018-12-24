from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters 
from rest_framework import generics


#local import 
from .serializers import UserProfileSerializer , HelloSerializer, ExampleSerializer,  ProgrammerSerializer, ParadigmSerializer, LanguageSerializer
from . import models 
from . import permissions


class APIView_class(APIView):
	#We make ever serializer class equal to variable "serializer_class". Try removing it and then you'll know what happens
	serializer_class = HelloSerializer

	def get(self, request, format=None):
		this_is_list = ['yellow', "red", "green"]
		return Response({"message": "this is sample json response", "list": this_is_list})


	def post(self, request):
		print(request.data)
		serializer = HelloSerializer(data= request.data)
		#checking if the data we got as the post request is valid. And the validators we used were mentioned in the serializer class. 
		if serializer.is_valid():
			name = serializer.data.get('name')
			message = 'Hello {}'.format(name)
			return Response({'message':message})

		else: 
			return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)


	#When we need to update or delete a particular flield, we use the primary key to find it. 
	def put(self, request, pk=None):
		return Response({'method':'put'})


	def patch(self, request, pk=None):
		return Response({'method':'patch'})


	def delete(self, request, pk=None):
		return Response({'method':'delete'})



class Viewset_class(viewsets.ViewSet):
	serializer_class = HelloSerializer

	
	def list(self, request):
		a_viewset = [
		"red", 
		"yellow",
		"green"
		]
		return Response({"message": "hello", "a_viewset": a_viewset})


	def create(self, request):
		serializer = HelloSerializer(data= request.data)
		if serializer.is_valid():
			name = serializer.data.get('name')
			message = 'Hello {}'.format(name)
			return Response({'message':message})

		else: 
			return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)


	def retrieve(self, request, pk=None):
		return Response({'method':'GET'})


	def update(self, request, pk=None):
		return Response({'method':'PUT'})


	def partial_update(self, request, pk=None):
		return Response({'method':'PATCH'})

	def destroy(self, request, pk=None):
		return Response({'method':'delete'})



class UserProfileViewSet(viewsets.ModelViewSet):
	serializer_class = UserProfileSerializer
	#we can also apply filters in this querysetc
	queryset = models.UserProfile.objects.all()
	authentication_classes = (TokenAuthentication,)#Type of authentication we'll use.
	permission_classes = (permissions.UpdateOwnProfile,)
	filter_backends = (filters.SearchFilter,)
	search_fields = ('name', 'email',)



class Example_APIView_class(APIView):
	def get(self, request, format=None):
		queryset = models.UserProfile.objects.all()
		serializers = ExampleSerializer(queryset,many=True)
		return Response(serializers.data)


#Same as the above class but here we are using generics view. 
class Example_APIView_generics_class(generics.ListAPIView):
	
	queryset = models.UserProfile.objects.all()
	serializer_class = ExampleSerializer
	def get_queryset(self):
		queryset = models.UserProfile.objects.all()
		query = self.request.GET.get('q')
		if query is not None: 
			queryset = queryset.filter(content__iscontains=query)

		return queryset













class ParadigmView(viewsets.ModelViewSet):
	queryset = models.Paradigm.objects.all()
	serializer_class = ParadigmSerializer


class LanguageView(viewsets.ModelViewSet):
	queryset = models.programmingLang.objects.all()
	serializer_class = LanguageSerializer


class ProgrammerView(viewsets.ModelViewSet):
	queryset = models.Programmer.objects.all()
	serializer_class = ProgrammerSerializer

























