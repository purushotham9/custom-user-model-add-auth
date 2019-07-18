# users/serializers.py
from rest_framework import serializers
from . import models
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MyUser
        fields = ('id', 'email', 'password', 'first_name', 'last_name', 'address', 'address_line2', 'city', 'state', 'zip_code', 'phone_number', 'month', 'day', 'year', 'security_number1', 'security_number2', 'security_number3', 'citizenship', 'marital_status', 'no_of_dependents', 'investment_experience', 'employment_status',  'employee_name', 'occupation', 'trade_options')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = models.MyUser.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user