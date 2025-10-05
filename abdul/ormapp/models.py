from django.db import models
from django.contrib import admin

class car(models.Model):
    model = models.CharField(max_length=20, help_text="CARS IDENTITY")
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    date = models.IntegerField()
    no = models.IntegerField()
    engine = models.CharField(max_length=100)
    length = models.IntegerField()

class carAdmin(admin.ModelAdmin):
    list_display = ('model', 'name', 'price', 'date', 'no', 'engine', 'length')
