from django.db import models


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
