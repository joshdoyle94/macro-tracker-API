from django.db import models
from .list import List

class Meal(models.Model):
    food_name = models.CharField(max_length=100)
    protein = models.IntegerField()
    carbohydrates = models.IntegerField()
    fats = models.IntegerField()
    calories = models.IntegerField()
    list = models.ForeignKey(
        List,
        on_delete=models.CASCADE,
        related_name='meals_tracked',
        null=True
    )


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.food_name} has been created."

    def as_dict(self):
        return {
            'id': self.id,
            'food_name': self.food_name,
            'protein': self.protein,
            'carbohydrates': self.carbohydrates,
            'fats': self.fats,
            'calories': self.calories
        }
