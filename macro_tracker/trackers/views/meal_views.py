from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


from ..models.meal import Meal
from ..serializers import MealSerializer, MealReadSerializer
# no authentication .
class MealsView(APIView):
    # View class for meals/ for viewing all and creating
    serializer_class = MealSerializer # making this alias is not doing us any good
    def get(self, request):
        meals = Meal.objects.all()
        serializer = MealReadSerializer(meals, many=True) # naming this serializer is misleading, it is the serialized data being stored in this variable not the serializer itself, also should be pluralized for the index
        return Response({'meals': serializer.data})

    def post(self, request):
        serializer = MealSerializer(data=request.data) # naming this serializer is misleading, it is the serialized data being stored in this variable not the serializer itself
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MealsDetailView(APIView):
    #  View class for meals/:pk
    serializer_class = MealSerializer # making this alias is not doing us any good 
    def get(self, request, pk):
        meal = get_object_or_404(Meal, pk=pk)
        serializer = MealReadSerializer(meal) # naming this serializer is misleading, it is the serialized data being stored in this variable not the serializer itself
        return Response({'meal': serializer.data})

    def patch(self, request, pk):
        meal = get_object_or_404(Meal, pk=pk)
        serializer = MealSerializer(meal, data=request.data) # naming this serializer is misleading, it is the serialized data being stored in this variable not the serializer itself
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        meal = get_object_or_404(Meal, pk=pk)
        meal.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)