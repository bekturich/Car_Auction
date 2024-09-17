from rest_framework import serializers
from .models import *
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

class UserSeriaLizer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'password', 'country', 'age', 'phone_number']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user

class LoginSeriaLizer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError('Неверные учетные данные')


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class UserProfileSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['username', 'age', 'phone_number']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CarMakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarMake
        fields = ['car_make_name']

class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model
        fields = ['model_name']

class CarSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    Car_Make = CarMakeSerializer()
    model = ModelSerializer()
    class Meta:
        model = Car
        fields = ['car_name', 'year', 'Car_Make', 'model', 'image', 'description', 'price', 'add_date', 'country', 'city', 'mileage', 'with_photo', 'drive', 'engine', 'transmission', 'volume', 'category']

class CarSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['car_name', 'price', 'city']

class AuctionSerializer(serializers.ModelSerializer):
    car = CarSimpleSerializer()
    end_date = serializers.DateTimeField(format('%d-%m-%Y %H:%M'))
    class Meta:
        model = Auction
        fields = '__all__'

class BidSerializer(serializers.ModelSerializer):
    user = UserProfileSimpleSerializer()
    car = CarSimpleSerializer()
    auction = AuctionSerializer()
    bid_time = serializers.DateTimeField(format('%d-%m-%Y %H:%M'))
    class Meta:
        model = Bid
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    order_date = serializers.DateTimeField(format('%d-%m-%Y %H:%M'))
    car = CarSimpleSerializer()
    class Meta:
        model = Order
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    order = OrderSerializer()
    payment_date = serializers.DateTimeField(format('%d-%m-%Y %H:%M'))
    class Meta:
        model = Payment
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    author = UserProfileSimpleSerializer()
    car = CarSimpleSerializer()
    created_date = serializers.DateTimeField(format('%d-%m-%Y %H:%M'))
    class Meta:
        model = Comment
        fields = '__all__'