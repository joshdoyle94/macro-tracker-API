from django.db import models


class List(models.Model):
    date = models.DateField()
    mental_rating = models.IntegerField()
    physical_rating = models.IntegerField()
    hours_slept = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Tracker: {self.date} has been created."

    def as_dict(self):
        return {
            'id': self.id,
            'date': self.date,
            'mental_rating': self.mental_rating,
            'physical_rating': self.physical_rating,
            'hours_slept': self.hours_slept,
        }
