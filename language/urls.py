from django.urls import path, include
from . import views 
from rest_framework import routers 
from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token


#this router will handle all the request like get, post, update and delete. We don't have to mention it implicitly.
router = routers.DefaultRouter()
#First arg is endpoint, and the second arg is the view
router.register('languages', views.LanguageView)
router.register('paradigm', views.ParadigmView)
router.register('programmer', views.ProgrammerView)
router.register('lol2', views.Viewset_class, base_name='lol2')
router.register('profile', views.UserProfileViewSet) #when registring modelViewSet, we don't need to use base_name.
#routers.url are being generated for us and we are jsut passing them. 

#when we are using a CBView, we use '.as_view()' method. 
urlpatterns = [
    path('lol/', views.APIView_class.as_view()),
    path('', include(router.urls)),
    path('test/', views.Example_APIView_class.as_view()), 
    path('test2/', views.Example_APIView_generics_class.as_view()), 
    url('auth-jwt/', obtain_jwt_token),
    url('auth-jwt-refresh/', refresh_jwt_token),
    url('auth-jwt-verify/', verify_jwt_token),
]
















