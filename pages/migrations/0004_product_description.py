# Generated by Django 5.1.1 on 2025-01-31 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_product_cartitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(default='설명 없음'),
        ),
    ]
