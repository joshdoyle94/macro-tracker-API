from django.contrib import admin
from trackers.models.list import List
from trackers.models.meal import Meal

# Register your models here.
admin.site.register(List)
admin.site.register(Meal)