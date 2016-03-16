from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from core.api.serializers import UserSerializer, ToDoSerializer
from django.contrib.auth.models import User
from core.models import ToDo
from rest_framework import viewsets

from rest_framework import permissions
# Create your views here.

class HolaMundo(APIView):
    def get(self, request, format=None):
        return Response({'mensaje': 'Hola Mundo desde Django Rest'})


hola_mundo = HolaMundo.as_view()



class Usuario(APIView):
    serializer_class = UserSerializer

    def get(self, request, format=None):
        users = User.objects.all()
        response = self.serializer_class(users, many=True)
        return Response(response.data)


usuarios = Usuario.as_view()




class TodoView(APIView):
    serializer_class = ToDoSerializer

    def get(self, request, id=None, format=None):
        todos = ToDo.objects.all()
        response = self.serializer_class(todos, many=True)
        return Response(response.data)

    def post(self, request, format=None):
        todo = self.serializer_class(data=request.data)
        if todo.is_valid():
            todo.save(propietario= request.user)
            return Response(todo.data)
        else:
            return Response(todo.errors)



todoview = TodoView.as_view()

class UserViewset(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = 'id'


class ToDoViewset(viewsets.ModelViewSet):
    serializer_class = ToDoSerializer
    queryset = ToDo.objects.all()
    lookup_field = 'id'
    permission_classes = (permissions.DjangoModelPermissions, )

    def perform_create(self, serializer):
        serializer.save(propietario=self.request.user)

    def list(self, request, *args, **kwargs):
        print request.user
        return super(ToDoViewset, self).list(request, *args, **kwargs)

        