
from rest_framework import serializers
from .models import Sales


class SalesQuerySerliazer(serializers.ModelSerializer):
    class Meta:
        model=Sales
        fields = "__all__"

        

class SalesSerliazer(serializers.ModelSerializer):
    class Meta:
        model=Sales
        exclude = ('id', )
        