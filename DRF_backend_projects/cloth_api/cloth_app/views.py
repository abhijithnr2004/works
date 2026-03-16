from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

from .models import Clothing
from .serializers import ClothingSerializers,UserSerializer



class ClothingCreateListView(APIView):

    authentication_classes = [authentication.BasicAuthentication]

    permission_classes = [permissions.IsAuthenticated]


    def post(self, request, *args, **kwargs):

        data = request.data

        serializer_instance = ClothingSerializers(data=data)

        if serializer_instance.is_valid():

            Clothing.objects.create(**data)

            return Response(data=serializer_instance.data)

        else:

            return Response(data=serializer_instance.errors)



    def get(self, request, *args, **kwargs):

        qs = Clothing.objects.all()

        serializer_instance = ClothingSerializers(qs, many=True)

        return Response(data=serializer_instance.data)




class ClothingRetrieveUpdateDeleteView(APIView):


    def get(self, request, *args, **kwargs):

        id = kwargs.get("pk")

        qs = Clothing.objects.get(id=id)

        serializer_instance = ClothingSerializers(qs)

        return Response(data=serializer_instance.data)



    def put(self, request, *args, **kwargs):

        id = kwargs.get("pk")

        serializer_instance = ClothingSerializers(data=request.data)

        if serializer_instance.is_valid():

            cleaned_data = serializer_instance.validated_data

            Clothing.objects.filter(id=id).update(**cleaned_data)

            return Response(data=serializer_instance.data)

        else:

            return Response(data=serializer_instance.errors)



    def delete(self, request, *args, **kwargs):

        id = kwargs.get("pk")

        Clothing.objects.get(id=id).delete()

        return Response({"message": "Deleted"})
class SignUpView(APIView) :

    def post(self,request,*args,**kwargs) :

        data = request.data

        serializer_instance = UserSerializer(data=data)

        if serializer_instance.is_valid() :

            cleaned_data = serializer_instance.validated_data

            User.objects.create_user(**cleaned_data)

            return Response(data=serializer_instance.data)
        
        else :

            return Response(data=serializer_instance.errors)