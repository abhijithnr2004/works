from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from gosell_app.serializers import UserSerializer,Vehicleserializer
from rest_framework import authentication,permissions,serializers
from gosell_app.models import Vehicle

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



class VehicleListCreateView(APIView):

    authentication_classes=[authentication.BasicAuthentication]

    permission_classes=[permissions.IsAuthenticated]

    def post(self,request,*args,**kwargs):

        data = request.data

        seraializer_instance = Vehicleserializer(data=request.data)

        if seraializer_instance.is_valid():

            cleaned_data = seraializer_instance.validated_data

            Vehicle.objects.create(**cleaned_data,owner=request.user) 

            return Response(data=seraializer_instance.data)
        else:
            return Response(data=seraializer_instance.errors)
        
    def get(self,request,*args,**kwargs) :

        user = request.user 

        qs = Vehicle.objects.filter(owner=user)

        serializer_instance = Vehicleserializer(qs,many = True)

        return Response(data=serializer_instance.data)
    
class VehicleRetrieveUpdateDeleteView(APIView) :

    authentication_classes = [authentication.BasicAuthentication]

    permission_classes = [permissions.IsAuthenticated]

    def get(self,request,*args,**kwargs) :

        id = kwargs.get("pk")

        Vehicle_object = Vehicle.objects.filter(id=id)

        if Vehicle_object.owner != request.user :

            raise serializers.ValidationError("owner permission required")
        
        serializer_instance = Vehicleserializer(Vehicle_object)

        return Response(data=serializer_instance.data)
    
    def delete(self,request,*args,**kwargs) :

        id = kwargs.get("pk")

        Vehicle_object = Vehicle.objects.get(id=id)

        if Vehicle_object.owner != request.user :

            raise serializers.ValidationError("owner permission required")
        
        Vehicle_object.delete()

        return Response(data={"message":"deleted"})
    
    def put(self,request,*args,**kwargs) :

        id = kwargs.get("pk")

        data = request.data

        Vehicle_object = Vehicle.objects.get(id=id)

        if Vehicle_object.owner != request.user :

            raise serializers.ValidationError("owner permissiom required")

        serializer_instance = Vehicleserializer(data=data,instance=Vehicle_object)

        if serializer_instance.is_valid() :

            serializer_instance.save()

            return Response(data=serializer_instance.data)
        
        else :

            return Response(serializer_instance.errors)
        




