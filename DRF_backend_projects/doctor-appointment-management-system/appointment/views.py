from django.shortcuts import render

from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView

from rest_framework import authentication, permissions

from appointment.serializers import UserSerializer, AppointmentSerializer
from appointment.models import Appointment
from appointment.permissions import IsOwner


class UserSignUpView(CreateAPIView):

    permission_classes = [permissions.AllowAny]

    serializer_class = UserSerializer


class AppointmentCreateListView(ListCreateAPIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = AppointmentSerializer

    def get_queryset(self):
        return Appointment.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)
    


class AppointmentReatrievUpdateDeleteView(RetrieveUpdateDestroyAPIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsOwner]

    serializer_class = AppointmentSerializer

    def get_queryset(self):
        return Appointment.objects.all()


