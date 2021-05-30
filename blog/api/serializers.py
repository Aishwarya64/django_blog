from rest_framework import serializers
from blog.models import Post

class PostSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title','context','date_posted','author']
