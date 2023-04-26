from rest_framework import serializers
from articles.models import Article, Comment

class ArticleSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    def get_user(self, obj):
        return obj.user.email  #article의 author의 email값
    
    class Meta:
        model = Article
        fields = '__all__'

class ArticleListSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.email  #article의 author의 email값

    class Meta:
        model = Article
        fields = ['pk','title','image','updated_at','user']


class ArticleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['title','image','content']


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.email  #article의 author의 email값

    class Meta:
        model = Comment
        fields = '__all__'


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['content',]
