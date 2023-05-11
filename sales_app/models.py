from django.db import models

# Create your models here.
class Sales(models.Model):
    order_id = models.CharField(max_length=50)
    order_date = models.DateField()
    ship_date = models.DateField()
    ship_mode = models.CharField(max_length=50)
    customer_id = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    segment = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    postal_code = models.IntegerField(blank=True, null=True)
    region = models.CharField(max_length=50)
    product_id = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    sub_category = models.CharField(max_length=50)
    product_name = models.CharField(max_length=200)
    sales = models.FloatField()

