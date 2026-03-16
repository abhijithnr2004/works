from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication,permissions,serializers
from employee_manage.serializers import UserSerializer,EmployeeSerializer
from employee_manage.models import Employee
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView,CreateAPIView
# Create your views here.
class SignUpView(CreateAPIView) :

    serializer_class = UserSerializer

class EmployeeCreateListView(ListCreateAPIView) :

    authentication_classes=[authentication.BasicAuthentication]

    permission_classes = [permissions.IsAuthenticated]

    serializer_class = EmployeeSerializer

    def perform_create(self, serializer):

        return Employee.objects.create(owner = self.request.user)
    
    def get_queryset(self):
        return Employee.objects.filter(owner = self.request.user)

    
class EmployeeRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView) :

    authentication_classes = [authentication.BasicAuthentication]

    permission_classes = [permissions.IsAuthenticated]

    serializer_class = EmployeeSerializer
    





        

