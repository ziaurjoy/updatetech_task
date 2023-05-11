
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


class TotalCountOfDistinctCustomersSerliazer(serializers.Serializer):
    city = serializers.DateField()
    coustomers = serializers.IntegerField()


class Top3CustomerstotalAmountOfTransactionsSerliazer(serializers.ModelSerializer):
    amount = serializers.IntegerField()
    class Meta:
        model=Sales
        fields = ['customer_name', 'amount']


class CustomerTransactionsPerYearSerliazer(serializers.Serializer):
    customer_name = serializers.CharField()
    year = serializers.DateField()
    transaction = serializers.IntegerField()


class MostSellingItemsSubCategorySerliazer(serializers.Serializer):
    sub_category = serializers.CharField()
    total = serializers.IntegerField()


class RegionBasisSalesPerformancePieChartSerliazer(serializers.ModelSerializer):
    sales = serializers.IntegerField()
    class Meta:
        model=Sales
        fields = ['region', 'sales']
        


class SalesPerformanceLineChartOverTheYearsSerliazer(serializers.Serializer):
    year = serializers.DateField()
    sales = serializers.IntegerField()


        