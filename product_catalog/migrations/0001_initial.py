# Generated by Django 2.2.7 on 2019-11-19 19:03

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCatalog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.CharField(editable=False, max_length=100)),
                ('code', models.CharField(blank=True, max_length=30, null=True)),
                ('available', models.BooleanField(default=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Products Catalog',
                'db_table': 'product_catalog',
            },
        ),
        migrations.CreateModel(
            name='ProductPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.PositiveIntegerField(default=0)),
                ('from_date', models.DateTimeField(default=datetime.datetime.now)),
                ('to_date', models.DateTimeField(blank=True, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_prices', to='product_catalog.ProductCatalog')),
            ],
            options={
                'verbose_name_plural': 'Product Prices',
                'db_table': 'product_price',
            },
        ),
        migrations.CreateModel(
            name='ProductAttribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(blank=True, max_length=30, null=True)),
                ('size', models.CharField(blank=True, max_length=30, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_attributes', to='product_catalog.ProductCatalog')),
            ],
            options={
                'verbose_name_plural': 'Product Attributes',
                'db_table': 'product_attribute',
            },
        ),
    ]
