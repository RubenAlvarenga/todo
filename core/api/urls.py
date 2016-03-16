from django.conf.urls import url, patterns, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter 
from core.api.views import UserViewset, ToDoViewset

router = DefaultRouter()
router.register(r'usuarios', UserViewset)
router.register(r'todo', ToDoViewset)



urlpatterns = patterns('',
	url(r'^hola_mundo_rest/$',  'core.api.views.hola_mundo'),
	#url(r'^usuarios/$',  'core.api.views.usuarios'),
	url(r'^', include(router.urls)),
	#url(r'^todo/$',  'core.api.views.todoview'),

)






