# Generated by Django 4.2.1 on 2023-05-10 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sales_app', '0006_delete_sales'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(max_length=50)),
                ('order_date', models.DateField()),
                ('ship_date', models.DateField()),
                ('ship_mode', models.CharField(max_length=50)),
                ('customer_id', models.CharField(max_length=50)),
                ('customer_name', models.CharField(max_length=50)),
                ('segment', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('postal_code', models.IntegerField(blank=True, null=True)),
                ('region', models.CharField(max_length=50)),
                ('product_id', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
                ('sub_category', models.CharField(max_length=50)),
                ('product_name', models.CharField(max_length=200)),
                ('sales', models.FloatField()),
            ],
        ),
    ]
