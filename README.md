# Ex02 Django ORM Web Application
## Date: 05.10.2025

## AIM
To develop a Django application to store and retrieve data from a Car Inventory Database using Object Relational Mapping(ORM).





## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
admin.py

from django.contrib import admin
from .models import (car,carAdmin)
admin.site.register(car, carAdmin)

models.py

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


```
## OUTPUT

![alt text](<Screenshot 2025-10-05 100621.png>)


## RESULT
Thus the program for creating car inventory database database using ORM hass been executed successfully
