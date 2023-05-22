from rest_framework import serializers
from .models import Book,BuyBook,Comment

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class BuySerializer(serializers.ModelSerializer):
    class Meta:
        model = BuyBook
        fields = '__all__'

class CommentSerializerr(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'