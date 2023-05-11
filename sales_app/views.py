
from sales_app.models import Sales
from sales_app.serializers import SalesQuerySerliazer, SalesSerliazer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.db.models import Count, Sum
from django.db.models.functions import TruncYear
import json
import pandas as pd
import matplotlib.pyplot as plt

# Create your views here.


class SalesViewSet(viewsets.ViewSet):
    def list(self, request):
        try:
            queryset = Sales.objects.all()
            serializer = SalesQuerySerliazer(queryset, many=True)
            response_data = {
                "data": serializer.data,
                "message": "Sales List Response Success",
                "error": False,
                "status": status.HTTP_200_OK

            }
            return Response(response_data)
        except Exception:
            response_data = {
                "message": "Error Response",
                "error": True,
                "status": status.HTTP_400_BAD_REQUEST

            }
            return Response(response_data)


    def create(self, request):
        try:
            serializer = SalesSerliazer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            response_data = {
                "data": serializer.data,
                "message": "Sales Registration Successfully",
                "error": False,
                "status": status.HTTP_201_CREATED

            }
            return Response(response_data)
        except Exception:
            response_data = {
                "message": "Sales Registration Error",
                "error": True,
                "status": status.HTTP_400_BAD_REQUEST

            }
            return Response(response_data)


    def retrieve(self, request, pk=None):
        try:
            sale = Sales.objects.get(id=pk)
            serializer = SalesQuerySerliazer(sale)
            response_data = {
                "data": serializer.data,
                "message": "Sales Retrieve Data",
                "error": False,
                "status": status.HTTP_201_CREATED

            }
            return Response(response_data)
        except Exception:
            response_data = {
                "message": "Sales Retrieve Error",
                "error": False,
                "status": status.HTTP_400_BAD_REQUEST

            }
            return Response(response_data)


    def update(self, request, pk=None):
        try:
            queryset = Sales.objects.get(id=pk)
            serializer = SalesSerliazer(queryset, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            response_data = {
                "data": serializer.data,
                "message": "Sales Update Successfully",
                "error": False,
                "status": status.HTTP_201_CREATED
            }
            return Response(response_data)
        except Exception:
            response_data = {
                "message": "Sales Update Error",
                "error": True,
                "status": status.HTTP_400_BAD_REQUEST
            }
            return Response(response_data)


    def destroy(self, request, pk=None):
        try:
            sale = Sales.objects.get(id=pk)
            sale.delete()
            response_data = {
                "message": "Sales Delete Successfully",
                "error": False,
                "status": status.HTTP_202_ACCEPTED
            }
            return Response(response_data)
        except Exception:
            response_data = {
                "message": "Sales Delete Error",
                "error": True,
                "status": status.HTTP_400_BAD_REQUEST
            }
            return Response(response_data)
        





class QueryViewSet(viewsets.ViewSet):

    # def list(self, request):
    #     queryset = Sales.objects.annotate(year=TruncYear('order_date')).values('year').annotate(count=Count('id')).order_by('year')
    #     return Response(queryset)

    # def list(self, request):
    #     queryset = Sales.objects.values('city').annotate(count=Count('customer_name')).order_by('city')
    #     return Response(queryset)
    
    # def list(self, request):
    #     queryset = Sales.objects.values('customer_name').annotate(Sum('sales')).order_by('sales__sum')
    #     print(queryset)
    #     return Response(queryset)


    # def list(self, request):
    #     queryset = Sales.objects.annotate(year=TruncYear('order_date')).values('customer_name', 'year').annotate(Sum('sales')).order_by('year').order_by('customer_name')
    #     return Response(queryset)
    
    # def list(self, request):
    #     queryset = Sales.objects.values('sub_category').annotate(Count('id')).order_by('-id__count')
    #     return Response(queryset)
    


    # def list(self, request):

    #     # Aggregate sales by region
    #     sales_by_region=Sales.objects.values('region').annotate(Sum('sales')).order_by('region')

    #     # Create a DataFrame from the query results
    #     df = pd.DataFrame(sales_by_region)
    #     print(df)
    #     # Create a pie chart from the DataFrame
    #     fig, ax = plt.subplots()
    #     df.plot.pie(y='sales__sum', labels=df['region'], ax=ax, autopct='%1.1f%%')

    #     # Set the title
    #     ax.set_title('Regional Sales Performance')

    #     # Save the chart to a PNG file
    #     fig.savefig('sales_performance.png')

    #     # Return the chart as a JSON response
    #     with open('sales_performance.png', 'rb') as f:
    #         data = f.read()
    #     # return JsonResponse({'chart': data}, content_type='image/png')
    #     return Response(content_type='image/png')



    def list(self, request):

        # Aggregate sales by region
        sales_by_region=Sales.objects.annotate(year=TruncYear('order_date')).values('year').annotate(Sum('sales')).order_by('year')

        # Create a DataFrame from the query results
        df = pd.DataFrame(sales_by_region)
        print(df)
        # Create a pie chart from the DataFrame
        fig, ax = plt.subplots()
        df.plot.pie(y='sales__sum', labels=df['year'], ax=ax, autopct='%1.1f%%')

        # Set the title
        ax.set_title('Year Sales Performance')

        # Save the chart to a PNG file
        fig.savefig('sales_performance_of_year.png')

        # Return the chart as a JSON response
        with open('sales_performance_of_year.png', 'rb') as f:
            data = f.read()
        # return JsonResponse({'chart': data}, content_type='image/png')
        return Response(content_type='image/png')



    # def retrieve(self, request, pk=None):
    #     queryset = Sales.objects.all()
    #     user = get_object_or_404(queryset, pk=pk)
    #     serializer = SalesSerliazer(user)
    #     return Response(serializer.data)