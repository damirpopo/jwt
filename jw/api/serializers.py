from rest_framework import serializers
from .models import OrderBook,Book


class BookSerializers(serializers.ModelSerializer):
    user=serializers.HiddenField(default=serializers.CurrentUserDefault)
    class Meta:
        model = Book
        fields = '__all__'


class OrderBookSerializers(serializers.ModelSerializer):
    user=serializers.HiddenField(default=serializers.CurrentUserDefault)
    class Meta:
        model = Book
        fields = '__all__'
