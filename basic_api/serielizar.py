from rest_framework import serializers
from .models import Article

#  USING SERIALIZER  (THE CODE IS REPEATING)

# class ArticleSerielizer(serializers.Serializer):
#     title = serializers.CharField(max_length=100)
#     body = serializers.CharField(max_length=200)
#     author = serializers.CharField(max_length=100)
#     email = serializers.EmailField(max_length=100)
#     date = serializers.DateField(auto_now_add=True)

#     def create(self, validated_data):
#         return Article.objects.create(validated_data)

#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.body = validated_data.get('body', instance.body)
#         instance.author = validated_data.get('author', instance.author)
#         instance.email = validated_data.get('email', instance.email)
#         instance.date = validated_data.get('date', instance.date)
#         instance.save()

#         return instance


# USING MODEL SERIELIZER
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'body', 'author', 'email', 'date']