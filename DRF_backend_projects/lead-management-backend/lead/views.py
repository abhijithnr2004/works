from django.shortcuts import render
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models import Count

from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework import authentication, permissions
from rest_framework.response import Response

from lead.serializers import UserSerializer, LeadSerializer
from lead.models import Lead


class UserSignUpView(CreateAPIView):

    serializer_class = UserSerializer


class LeadCreateList(CreateAPIView, ListAPIView):

    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = LeadSerializer

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Lead.objects.filter(owner=self.request.user)


class LeadRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):

    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = LeadSerializer

    lookup_field = 'pk'

    def get_queryset(self):
        return Lead.objects.filter(owner=self.request.user)


class LeadSummaryView(APIView):

    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):

        current_date = timezone.now()

        current_month = current_date.month

        current_year = current_date.year

        qs = Lead.objects.filter(owner=request.user,
                                 created_at__year=current_year,
                                 created_at__month=current_month)
        
        month_wise_total_leads = qs.aggregate(total=Count('owner'))

        source_wise_total_leads = qs.values('source').annotate(total=Count('owner'))

        status_wise_total_leads = qs.values('status').annotate(total=Count('owner'))

        context = {
            "month_wise_total_leads" : month_wise_total_leads,
            "source_wise_total_leads" : source_wise_total_leads,
            "status_wise_total_leads" : status_wise_total_leads

        }

        return Response(data=context)
    








        

