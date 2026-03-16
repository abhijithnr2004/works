from rest_framework import serializers

from api.models import Movie



class MovieSerializer(serializers.Serializer):

    id = serializers.CharField(read_only=True)

    title = serializers.CharField()

    year = serializers.CharField()

    language = serializers.CharField()

    genre = serializers.ChoiceField(Movie.GENRE_OPTIONS)

    run_time = serializers.IntegerField()

    director = serializers.CharField()



    def validate(self, data):
        
        if data.get("run_time") < 60 and data.get("run_time") > 360:

            raise serializers.ValidationError("runtime should be > 60 and < 360")
        

        title = data.get("title")

        qs = Movie.objects.filter(title=title)

        if qs.exists():

            raise serializers.ValidationError("movie already exists")
        

        # if data.get("id") not in Movie.objects.get("id") :

        #     raise serializers.ValidationErrorz("movie with the id not found")
        
        return data
    
class UserSerializer(serializers.Serializer) :

    username = serializers.CharField()

    first_name = serializers.CharField()

    last_name = serializers.CharField()

    email = serializers.EmailField()

    password = serializers.CharField()
