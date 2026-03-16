from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from jobs.models import Job
from jobs.serializers import JobSerializer


class JobCreateListView(APIView):

    def post(self, request, *args, **kwargs):

        serializer_instance = JobSerializer(data=request.data)

        if serializer_instance.is_valid():

            cleaned_data = serializer_instance.validated_data

            Job.objects.create(**cleaned_data)

            return Response(data=serializer_instance.data)
        
        else:

            return Response(data=serializer_instance.errors)
        

    
    def get(self, request, *args, **kwargs):

        qs = Job.objects.all()

        serializer_instance = JobSerializer(qs, many=True)

        return Response(data=serializer_instance.data)





class JobRetrieveUpdateDeleteView(APIView):

    def get(self, request, *args, **kwargs):

        id = kwargs.get("pk")

        qs = Job.objects.get(id=id)

        serializer_instance = JobSerializer(qs)

        return Response(data=serializer_instance.data)
    


    def put(self, request, *args, **kwargs):

        id = kwargs.get("pk")

        data = request.data

        serializer_instance = JobSerializer(data=data)

        if serializer_instance.is_valid():

            cleaned_data = serializer_instance.validated_data

            Job.objects.filter(id=id).update(**cleaned_data)

            return Response(data=serializer_instance.data)
        
        else:

            return Response(data=serializer_instance.errors)
        
    
    def delete(self, request, *args, **kwargs):

        id = kwargs.get("pk")

        Job.objects.filter(id=id).delete()

        return Response({"message" : "Deleted"})

