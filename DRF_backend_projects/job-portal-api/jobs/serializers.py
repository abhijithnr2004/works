from rest_framework import serializers

from jobs.models import Job


class JobSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only = True)

    title = serializers.CharField()

    company = serializers.CharField()

    location = serializers.CharField()

    job_type = serializers.ChoiceField(choices = Job.JOB_TYPE_CHOICES)

    experience = serializers.IntegerField()

    salary = serializers.IntegerField()

    skills = serializers.CharField()

    is_remote = serializers.BooleanField()

    is_active = serializers.BooleanField()

    posted_date = serializers.DateTimeField(read_only = True)

    def validate(self, data):

        if data.get("salary") < 10000 :

            raise serializers.ValidationError("Salary must be greater than 10000")

        if data.get("experience") < 0 or data.get("experience") > 30 :

            raise serializers.ValidationError("Experience must be greater than 0 or less than 30")
        
        


