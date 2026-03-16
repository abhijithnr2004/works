from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth.models import User

from electronics.serializers import UserSerializer,ElectronicProductSerializer
from electronics.models import ElectronicProduct
from rest_framework.response import Response
from rest_framework import authentication,permissions,serializers


# Create your views here.


class SignUpView(APIView) :

    def post(self,request,*args,**kwargs) :

        data = request.data

        serializer_instance = UserSerializer(data=data)

        if serializer_instance.is_valid() :

            cleaned_data = serializer_instance.validated_data

            User.objects.create_user(**cleaned_data)

            return Response(data=serializer_instance.data)
        
        else:

            return Response(data=serializer_instance.errors)
        
class ElectronicProductListCreateView(APIView):

    authentication_classes=[authentication.BasicAuthentication]

    permission_classes=[permissions.IsAuthenticated]

    def post(self,request,*args,**kwargs):

        data = request.data

        seraializer_instance = ElectronicProductSerializer(data=request.data)

        if seraializer_instance.is_valid():

            cleaned_data = seraializer_instance.validated_data

            ElectronicProduct.objects.create(**cleaned_data,owner=request.user) 

            return Response(data=seraializer_instance.data)
        else:
            return Response(data=seraializer_instance.errors)
        
    def get(self,request,*args,**kwargs) :

        user = request.user 

        qs = ElectronicProduct.objects.filter(owner=user)

        serializer_instance = ElectronicProductSerializer(qs,many = True)

        return Response(data=serializer_instance.data)
    
class ElectronicProductRetrieveUpdateDeleteView(APIView) :

    authentication_classes = [authentication.BasicAuthentication]

    permission_classes = [permissions.IsAuthenticated]

    def get(self,request,*args,**kwargs) :

        id = kwargs.get("pk")

        ElectronicProduct_object = ElectronicProduct.objects.get(id=id)

        if ElectronicProduct_object.owner != request.user :

            raise serializers.ValidationError("owner permission required")
        
        serializer_instance = ElectronicProductSerializer(ElectronicProduct_object)

        return Response(data=serializer_instance.data)
    
    def delete(self,request,*args,**kwargs) :

        id = kwargs.get("pk")

        ElectronicProduct_object = ElectronicProduct.objects.get(id=id)

        if ElectronicProduct_object.owner != request.user :

            raise serializers.ValidationError("owner permission required")
        
        ElectronicProduct_object.delete()

        return Response(data={"message":"deleted"})
    
    def put(self,request,*args,**kwargs) :

        id = kwargs.get("pk")

        data = request.data

        ElectronicProduct_object = ElectronicProduct.objects.get(id=id)

        if ElectronicProduct_object.owner != request.user :

            raise serializers.ValidationError("owner permissiom required")

        serializer_instance = ElectronicProductSerializer(data=data,instance=ElectronicProduct_object)

        if serializer_instance.is_valid() :

            serializer_instance.save()

            return Response(data=serializer_instance.data)
        
        else :

            return Response(serializer_instance.errors)