from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Card


class CardModelSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Card
        fields = ('id', 'title', 'detail', 'relevance', 'owner')


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')
