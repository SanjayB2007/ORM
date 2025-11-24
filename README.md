# Ex01 Django ORM Web Application
## Date:22-11-2025

## AIM
To develop a Django Application to store and retrieve data from a E-Commerce Website Database for Amazon or Flipkart using Object Relational Mapping(ORM).





## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Detect changes and create migration files that describe how to modify the database schema

### STEP 5:
Execute the migration files and update the database schema to match your Django models

### STEP 6:
Create a superuser with full access rights to all models and data through the admin interface.

### STEP 7:
Apply the migration files of the created app to the database

### STEP 8:
Execute Django admin using localhost and create details for 10 entries

## PROGRAM
```
model.py

from django.db import models
from django.contrib import admin
class items(models.Model):
    product_name=models.CharField(max_length=100)
    product_id=models.IntegerField(primary_key=True)
    product_type=models.CharField(max_length=100)
    product_price=models.IntegerField()
    warranty=models.CharField(max_length=10)
    return_or_replacement_policy=models.TextField()
    seller_contact=models.IntegerField()
    seller_contact=models.EmailField()
class itemsAdmin(admin.ModelAdmin):
    list_display=["product_name","product_id","product_type","product_price","warranty","return_or_replacement_policy","seller_contact","seller_contact"]

admin.py
```
from django.contrib import admin

# Register your models here.
from .models import items,itemsAdmin
admin.site.register(items,itemsAdmin)
```
## OUTPUT



## RESULT
Thus the program for creating E-commerce website database using ORM hass been executed successfully
