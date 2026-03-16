from django.shortcuts import render
from django.db.models import Sum, aggregates
from django.utils import timezone

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework import serializers
from rest_framework.generics import CreateAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView

from transaction.serializers  import UserSerializer, ExpenseSerializer
from transaction.models import Expense
from transaction.permissions import IsOwner

class SignUpView(CreateAPIView):

    serializer_class = UserSerializer

class ExpenseCreateListView(ListCreateAPIView):

    serializer_class = ExpenseSerializer

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsOwner]

    def perform_create(self, serializer):
        
        return serializer.save(owner = self.request.user)
    
    def get_queryset(self):

        return Expense.objects.filter(owner = self.request.user)

class ExpenseRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):

    serializer_class = ExpenseSerializer

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsOwner]

    queryset = Expense.objects.all()


class ExpenseSummaryView(APIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsOwner]


    def get(self, request, *args, **kwargs):

        cur_data = timezone.now() ## get current date

        cur_month = cur_data.month  ## current date month

        cur_year = cur_data.year  ## current date year

        qs = Expense.objects.filter(
            owner = request.user,
            created_at__month = cur_month,
            created_at__year = cur_year
        )

        total_expense = qs.values('amount').aggregate(total_exp = (Sum('amount')))

        print(total_expense)

        category_wise_sum = qs.values("category").annotate(total = Sum('amount'))


        return Response(data = {"message" : "OK"})
    

