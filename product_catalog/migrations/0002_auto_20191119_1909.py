# Generated by Django 2.2.7 on 2019-11-19 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcatalog',
            name='slug',
            field=models.SlugField(editable=False, unique=True),
        ),
    ]
