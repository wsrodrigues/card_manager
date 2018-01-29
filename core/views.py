from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import permissions
from .models import Card
from .serializers import CardModelSerializer, UserModelSerializer


class CardList(generics.ListCreateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardModelSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CardDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Card.objects.all()
    serializer_class = CardModelSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
