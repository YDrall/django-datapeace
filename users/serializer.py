from datetime import datetime

from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    age = serializers.IntegerField()

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'company_name', 'age', 'city', 'state', 'zip', 'email', 'web')
        order_by = 'id'
