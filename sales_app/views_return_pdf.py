
from sales_app.models import Sales
from sales_app.serializers import SalesQuerySerliazer, SalesSerliazer
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.db.models import Count, Sum
from django.db.models.functions import TruncYear
import json
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
        


    

class SalesReportTotalNumberOfOdersCountPerYearReportViewView(generics.ListAPIView):

    def get_queryset(self):
        return Sales.objects.annotate(year=TruncYear('order_date')).values('year').annotate(count=Count('id')).order_by('year')

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        # generate PDF report
        buffer = BytesIO()
        pdf = canvas.Canvas(buffer)
        pdf.setTitle("Total number of orders count per year")
        pdf.drawString(70, 730, "Total Number Of Orders Count Per Year Report")
        y = 700
        # add content to PDF report
        pdf.drawString(70, y, "#")
        pdf.drawString(140, y, "Year")
        pdf.drawString(210, y, "Count")
        i = 1
        for sale in queryset:
            y -= 25
            pdf.drawString(70, y, str(i))
            pdf.drawString(140, y, str(sale['year'].year))
            pdf.drawString(210, y, str(sale['count']))
            i += 1
            
        pdf.showPage()
        pdf.save()
        pdf_data = buffer.getvalue()
        buffer.close()
        with open('Total number of orders count per year report.pdf', 'wb') as f:
            f.write(pdf_data)
        response = FileResponse(io.BytesIO(pdf_data), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="Total number of orders count per year report.pdf"'
        return response



class TotalCountOfDistinctCustomersViewView(generics.ListAPIView):

    def get_queryset(self):
        return Sales.objects.values('city').annotate(count=Count('customer_name')).order_by('city')

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        # generate PDF report
        buffer = BytesIO()
        pdf = canvas.Canvas(buffer)
        pdf.setTitle("Total Count Of Distinct Customer Report")
        pdf.drawString(70, 730, "Total Count Of Distinct Customer Report")
        y = 700
        # add content to PDF report
        pdf.drawString(70, y, "#")
        pdf.drawString(140, y, "City")
        pdf.drawString(210, y, "Customer Count")
        i = 1
        for sale in queryset:
            y -= 25
            pdf.drawString(70, y, str(i))
            pdf.drawString(140, y, str(sale['city']))
            pdf.drawString(250, y, str(sale['count']))
            i += 1
            
        pdf.showPage()
        pdf.save()
        pdf_data = buffer.getvalue()
        buffer.close()
        with open('TotalCountOfDistinctCustomerReport.pdf', 'wb') as f:
            f.write(pdf_data)

        response = FileResponse(io.BytesIO(pdf_data), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="TotalCountOfDistinctCustomerReport.pdf"'
        return response



class Top3CustomerstotalAmountOfTransactionsViewView(generics.ListAPIView):

    def get_queryset(self):
        return Sales.objects.values('customer_name').annotate(Sum('sales')).order_by('-sales__sum')[:3]

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        print(queryset)
        # generate PDF report
        buffer = BytesIO()
        pdf = canvas.Canvas(buffer)
        pdf.setTitle("Top3 Customers Total Amount Of Transactions Report")
        pdf.drawString(70, 730, "Top3 Customers Total Amount Of Transactions Report")
        y = 700
        # add content to PDF report
        pdf.drawString(70, y, "#")
        pdf.drawString(140, y, "Customer Name")
        pdf.drawString(250, y, "Transactions")
        i = 1
        for sale in queryset:
            y -= 25
            pdf.drawString(70, y, str(i))
            pdf.drawString(140, y, str(sale['customer_name']))
            pdf.drawString(250, y, str(sale['sales__sum']))
            i += 1
            
        pdf.showPage()
        pdf.save()
        pdf_data = buffer.getvalue()
        buffer.close()
        with open('Top3CustomerstotalAmountOfTransactions.pdf', 'wb') as f:
            f.write(pdf_data)

        response = FileResponse(io.BytesIO(pdf_data), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="Top3CustomerstotalAmountOfTransactions.pdf"'
        return response
    


class CustomerTransactionsPerYearReportViewView(generics.ListAPIView):

    def get_queryset(self):
        return Sales.objects.annotate(year=TruncYear('order_date')).values('customer_name', 'year').annotate(Sum('sales')).order_by('year').order_by('customer_name')

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        print(queryset)
        # generate PDF report
        buffer = BytesIO()
        pdf = canvas.Canvas(buffer)
        pdf.setTitle("Customer Transactions Per Year Report")
        pdf.drawString(70, 730, "Customer Transactions Per Year Report")
        y = 700
        # add content to PDF report
        pdf.drawString(70, y, "#")
        pdf.drawString(140, y, "Customer Name")
        pdf.drawString(250, y, "Year")
        pdf.drawString(350, y, "Transactions")
        i = 1
        for sale in queryset:
            y -= 25
            pdf.drawString(70, y, str(i))
            pdf.drawString(140, y, str(sale['customer_name']))
            pdf.drawString(250, y, str(sale['year']))
            pdf.drawString(350, y, str(sale['sales__sum']))
            i += 1
            
        pdf.showPage()
        pdf.save()
        pdf_data = buffer.getvalue()
        buffer.close()
        with open('CustomerTransactionsPerYearReport.pdf', 'wb') as f:
            f.write(pdf_data)

        response = FileResponse(io.BytesIO(pdf_data), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="CustomerTransactionsPerYearReport.pdf"'
        return response


class MostSellingItemsSubCategoryNamesView(generics.ListAPIView):

    def get_queryset(self):
        return Sales.objects.values('sub_category').annotate(Count('id')).order_by('-id__count')

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        print(queryset)
        # generate PDF report
        buffer = BytesIO()
        pdf = canvas.Canvas(buffer)
        pdf.setTitle("Most Selling Items Sub Category Names Report")
        pdf.drawString(70, 730, "Most Selling Items Sub Category Names Report")
        y = 700
        # add content to PDF report
        pdf.drawString(70, y, "#")
        pdf.drawString(140, y, "Sub Category")
        pdf.drawString(250, y, "Count")
        
        i = 1
        for sale in queryset:
            y -= 25
            pdf.drawString(70, y, str(i))
            pdf.drawString(140, y, str(sale['sub_category']))
            pdf.drawString(250, y, str(sale['id__count']))
            i += 1
            
        pdf.showPage()
        pdf.save()
        pdf_data = buffer.getvalue()
        buffer.close()
        with open('MostSellingItemsSubCategoryNameReport.pdf', 'wb') as f:
            f.write(pdf_data)

        response = FileResponse(io.BytesIO(pdf_data), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="MostSellingItemsSubCategoryNameReport.pdf"'
        return response
    



class RegionBasisSalesPerformancePieChartView(generics.ListAPIView):
    def get_queryset(self):
        return Sales.objects.values('region').annotate(Sum('sales')).order_by('region')
    
    def get(self, request, *args, **kwargs):
        sales_by_region = self.get_queryset()

        # Create a DataFrame from the query results
        df = pd.DataFrame(sales_by_region)
        print(df)
        # Create a pie chart from the DataFrame
        fig, ax = plt.subplots()
        df.plot.pie(y='sales__sum', labels=df['region'], ax=ax, autopct='%1.1f%%')

        # Set the title
        ax.set_title('Regional Sales Performance')

        # Save the chart to a PNG file
        fig.savefig('sales_performance.png')

        # Return the chart as a JSON response
        with open('sales_performance.png', 'rb') as f:
            data = f.read()

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
        with open('RegionBasisSalesPerformancePieChartReport.pdf', 'wb') as f:
            f.write(pdf_data)

        response = FileResponse(io.BytesIO(pdf_data), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="RegionBasisSalesPerformancePieChartReport.pdf"'
        return response
    

class SalesPerformanceLineChartOverTheYearsView(generics.ListAPIView):
    def get_queryset(self):
        return Sales.objects.annotate(year=TruncYear('order_date')).values('year').annotate(Sum('sales')).order_by('year')
    
    def get(self, request, *args, **kwargs):
        sales_performance_line = self.get_queryset()
        # Create a DataFrame from the query results
        df = pd.DataFrame(sales_performance_line)

        plt.plot(df['year'], df['sales__sum'])

        # Set the title and labels
        plt.title('Sales Performance Over the Years')
        plt.xlabel('year')
        plt.ylabel('sales__sum')
        plt.savefig('sales_performance.png')

        # Return the chart as a JSON response
        with open('sales_performance.png', 'rb') as f:
            data = f.read()

        buffer = BytesIO()
        pdf = canvas.Canvas(buffer)
        pdf.setTitle("Sales Performance Year Report")
        pdf.drawString(70, 730, "Sales Performance Year Report")

        # add content to PDF report
        y = 700
        pdf.drawInlineImage('sales_performance.png',15, y-450)

        pdf.showPage()
        pdf.save()
        pdf_data = buffer.getvalue()
        buffer.close()
        with open('sales_performance.pdf', 'wb') as f:
            f.write(pdf_data)

        response = FileResponse(io.BytesIO(pdf_data), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="sales_performance.pdf"'
        return response
        


