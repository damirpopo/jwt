from django.shortcuts import render
from .serializers import BookSerializers,OrderBookSerializers
from .models import Book,OrderBook
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateAPIView,RetrieveDestroyAPIView,ListAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly,IsAdminUser
from rest_framework.authentication import TokenAuthentication


class BookList(ListAPIView):
    queryset = Book
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = BookSerializers

class BookDestroyUpdate(RetrieveUpdateDestroyAPIView):
    queryset = Book
    permission_classes = (IsAdminUser,)
    serializer_class = BookSerializers

class OrderBookListCreate(ListCreateAPIView):
    queryset = OrderBook
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = OrderBookSerializers
