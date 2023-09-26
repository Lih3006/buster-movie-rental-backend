from rest_framework import serializers
from .models import MovieOrder, RatingMovie, Movie
from users.serializers import UserSerializer


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(max_length=10,required=False, default=None)
    rating = serializers.ChoiceField(choices=RatingMovie.choices, default=RatingMovie.G)
    synopsis = serializers.CharField(required=False, default=None)
    added_by = serializers.SerializerMethodField()
        
    def get_added_by(self, obj):
        return obj.user.email
    
    def create(self, validated_data):
        return Movie.objects.create(**validated_data)
    
    
class MovieOrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.SerializerMethodField()   
    buyed_at = serializers.DateTimeField(read_only=True)
    buyed_by = serializers.SerializerMethodField()
    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    
    def get_title(self,obj):
        return obj.movie.title
        
    def get_buyed_by(self,obj):
        return obj.user.email
    
    def create(self, validated_data):
        return MovieOrder.objects.create(**validated_data)
    