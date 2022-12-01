from rest_framework import serializers

from .models.list import List
from .models.meal import Meal

class ListSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = List

class ListReadSerializer(serializers.ModelSerializer):
    meal = serializers.StringRelatedField()
    class Meta:
        fields = '__all__'
        model = List

class MealSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Meal

class MealReadSerializer(serializers.ModelSerializer):
    list = serializers.StringRelatedField()
    class Meta:
        fields = '__all__'
        model = Meal