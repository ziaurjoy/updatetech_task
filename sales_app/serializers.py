
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


class TotalNumberOfOrdersCountPerYearSerliazer(serializers.Serializer):
    year = serializers.DateField()
    sales = serializers.IntegerField()


class TotalCountOfDistinctCustomers(serializers.Serializer):
    city = serializers.DateField()
    coustomers = serializers.IntegerField()


class Top3CustomerstotalAmountOfTransactionsSerliazer(serializers.ModelSerializer):
    sales__sum = serializers.IntegerField()
    class Meta:
        model=Sales
        fields = ['customer_name', 'sales__sum']


class CustomerTransactionsPerYearSerliazer(serializers.Serializer):
    customer_name = serializers.CharField()
    year = serializers.DateField()
    sales__sum = serializers.IntegerField()


class MostSellingItemsSubCategorySerliazer(serializers.Serializer):
    sub_category = serializers.CharField()
    total = serializers.IntegerField()


class RegionBasisSalesPerformancePieChartSerliazer(serializers.ModelSerializer):
    sales__sum = serializers.IntegerField()
    class Meta:
        model=Sales
        fields = ['region', 'sales__sum']
        


class SalesPerformanceLineChartOverTheYearsSerliazer(serializers.Serializer):
    year = serializers.DateField()
    sales = serializers.IntegerField()


        