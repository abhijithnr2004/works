from django.shortcuts import render

from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework import authentication, permissions,serializers

from poll_app.serializers import UserSerializer, PollSerializer, ChoiceSerializer, VoteSerializer
from poll_app.models import Poll,Choice





from poll_app.permissions import IsOwner



class UserSignUpView(CreateAPIView):

    permission_classes = [permissions.AllowAny]

    serializer_class = UserSerializer


class PollCreateListView(ListCreateAPIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = PollSerializer

    def  get_queryset(self):
        return Poll.objects.filter(is_active="True")
    
    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)
    

class PollRetrieveView(RetrieveAPIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = PollSerializer


    def  get_queryset(self):
        return Poll.objects.filter(is_active="True")
    


class PollDeleteView(DestroyAPIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsOwner]

    def  get_queryset(self):
        return Poll.objects.filter(is_active="True")
    

class ChoiceCreateListView(ListCreateAPIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsOwner]

    serializer_class = ChoiceSerializer

    def perform_create(self, serializer):

        id = self.kwargs.get("pk")

        poll_instance = Poll.objects.get(id=id)

        return serializer.save(poll_object=poll_instance)
    

class VoteCreateView(CreateAPIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = VoteSerializer

    def perform_create(self, serializer):

        id = self.kwargs.get("pk")

        poll_instance = Poll.objects.get(id=id)

        poll_valid_choices = Choice.objects.filter(poll_object = poll_instance)

        choice_object = serializer.validated_data.get("choice_object")

        if choice_object not in poll_valid_choices :

            raise serializers.ValidationError("invalid choice for poll")

        return serializer.save(poll_object=poll_instance, owner=self.request.user)
