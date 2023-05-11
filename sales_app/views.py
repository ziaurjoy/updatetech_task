
from sales_app.models import Sales
from sales_app import serializers
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Count, Sum
from django.db.models.functions import TruncYear


# if return pdf file
import pandas as pd
import matplotlib.pyplot as plt
from reportlab.pdfgen import canvas
from io import BytesIO
from django.http import FileResponse
import io
# Create your views here.


class SalesViewSet(viewsets.ViewSet):
    def list(self, request):
        try:
            queryset = Sales.objects.all()
            serializer = serializers.SalesQuerySerliazer(queryset, many=True)
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
            serializer = serializers.SalesSerliazer(data=request.data)
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
            serializer = serializers.SalesQuerySerliazer(sale)
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
            serializer = serializers.SalesSerliazer(queryset, data=request.data)
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
        


    
class TotalNumberOfOrdersCountPerYearView(generics.ListCreateAPIView):
    queryset = Sales.objects.annotate(year=TruncYear('order_date')).values('year').annotate(sales=Count('id')).order_by('year')
    serializer_class = serializers.TotalNumberOfOrdersCountPerYearSerliazer


class TotalCountOfDistinctCustomersView(generics.ListAPIView):
    queryset = Sales.objects.values('city').annotate(coustomers=Count('customer_name')).order_by('city')
    serializer_class = serializers.TotalCountOfDistinctCustomersSerliazer


class Top3CustomerstotalAmountOfTransactionsView(generics.ListAPIView):
    queryset = Sales.objects.values('customer_name').annotate(amount=Sum('sales')).order_by('-amount')[:3]
    serializer_class = serializers.Top3CustomerstotalAmountOfTransactionsSerliazer


class CustomerTransactionsPerYearReportView(generics.ListAPIView):
    queryset = Sales.objects.annotate(year=TruncYear('order_date')).values('customer_name', 'year').annotate(transaction=Sum('sales')).order_by('year').order_by('customer_name')
    serializer_class = serializers.CustomerTransactionsPerYearSerliazer


class MostSellingItemsSubCategoryView(generics.ListAPIView):
    queryset = Sales.objects.values('sub_category').annotate(total=Count('id')).order_by('-total')
    serializer_class = serializers.MostSellingItemsSubCategorySerliazer
    

class RegionBasisSalesPerformancePieChartView(generics.ListAPIView):
    queryset = Sales.objects.values('region').annotate(sales=Sum('sales')).order_by('region')
    serializer_class = serializers.RegionBasisSalesPerformancePieChartSerliazer
    


class SalesPerformanceLineChartOverTheYearsView(generics.ListAPIView):
    queryset = Sales.objects.annotate(year=TruncYear('order_date')).values('year').annotate(sales = Sum('sales')).order_by('year')
    serializer_class = serializers.SalesPerformanceLineChartOverTheYearsSerliazer




# if it's call to return to Pie Chart pdf file
class RegionBasisSalesPerformancePieChartReportView(generics.ListAPIView):
    def get_queryset(self):
        return Sales.objects.values('region').annotate(sales=Sum('sales')).order_by('region')
    
    def get(self, request, *args, **kwargs):
        sales_by_region = self.get_queryset()

        # Create a DataFrame from the query results
        df = pd.DataFrame(sales_by_region)
        print(df)
        # Create a pie chart from the DataFrame
        fig, ax = plt.subplots()
        df.plot.pie(y='sales', labels=df['region'], ax=ax, autopct='%1.1f%%')

        # Set the title
        ax.set_title('Regional Sales Performance')

        # Save the chart to a PNG file
        fig.savefig('sales_performance.png')

        buffer = BytesIO()
        pdf = canvas.Canvas(buffer)
        pdf.setTitle("Regional Sales Performance Report")
        pdf.drawString(70, 730, "Regional Sales Performance Report")

        # add content to PDF report
        y = 700
        pdf.drawInlineImage('sales_performance.png',15, y-450)

        pdf.showPage()
        pdf.save()
        pdf_data = buffer.getvalue()
        buffer.close()
        with open('SalesPerformancePieChartReport.pdf', 'wb') as f:
            f.write(pdf_data)

        response = FileResponse(io.BytesIO(pdf_data), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="SalesPerformancePieChartReport.pdf"'
        return response
    

