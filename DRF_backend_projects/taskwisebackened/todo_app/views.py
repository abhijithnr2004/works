from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from todo_app.serializers import UserSerializer,TaskSerializer
from rest_framework import authentication,permissions,serializers
from todo_app.models import Task

class SignUpView(APIView):

    def post(self,request,*args,**kwargs):

        data = request.data

        serializer_instance = UserSerializer(data=data) 

        if serializer_instance.is_valid():

            cleaned_data = serializer_instance.validated_data

            User.objects.create_user(**cleaned_data)

            return Response(data=serializer_instance.data)
        
        else:

            return Response(data=serializer_instance.errors)



class TaskListCreateView(APIView):

    authentication_classes=[authentication.BasicAuthentication]

    permission_classes=[permissions.IsAuthenticated]

    def post(self,request,*args,**kwargs):

        data = request.data

        seraializer_instance = TaskSerializer(data=request.data)

        if seraializer_instance.is_valid():

            # seraializer_instance.save(owner=request.user)

            cleaned_data = seraializer_instance.validated_data

            Task.objects.create(**cleaned_data,owner=request.user) 

            return Response(data=seraializer_instance.data)
        else:
            return Response(data=seraializer_instance.errors)
        
    def get(self,request,*args,**kwargs) :

        user = request.user 

        qs = Task.objects.filter(owner=user)

        serializer_instance = TaskSerializer(qs,many = True)

        return Response(data=serializer_instance.data)
    
class TaskRetrieveUpdateDeleteView(APIView) :

    authentication_classes = [authentication.BasicAuthentication]

    permission_classes = [permissions.IsAuthenticated]

    def get(self,request,*args,**kwargs) :

        id = kwargs.get("pk")

        task_object = Task.objects.get(id=id)

        if task_object.owner != request.user :

            raise serializers.ValidationError("owner permission required")
        
        serializer_instance = TaskSerializer(task_object)

        return Response(data=serializer_instance.data)
    
    def delete(self,request,*args,**kwargs) :

        id = kwargs.get("pk")

        task_object = Task.objects.get(id=id)

        if task_object.owner != request.user :

            raise serializers.ValidationError("owner permission required")
        
        task_object.delete()

        return Response(data={"message":"deleted"})
    
    def put(self,request,*args,**kwargs) :

        id = kwargs.get("pk")

        data = request.data

        task_object = Task.objects.get(id=id)

        if task_object.owner != request.user :

            raise serializers.ValidationError("owner permissiom required")

        serializer_instance = TaskSerializer(data=data,instance=task_object)

        if serializer_instance.is_valid() :

            serializer_instance.save()

            return Response(data=serializer_instance.data)
        
        else :

            return Response(serializer_instance.errors)
        




