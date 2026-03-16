from django.shortcuts import render

from billing.models import Customer

from billing.serializers import CustomerSerializer

from rest_framework.viewsets import ModelViewSet

from billing.permissions import IsAdminOwner
# Create your views here.

class CustomerViewSet(ModelViewSet):

    permission_classes = [IsAdminOwner]

    queryset = Customer.objects.all()

    serializer_class = CustomerSerializer

    def perform_create(self, serializer):

        serializer.save(owner=self.request.user)