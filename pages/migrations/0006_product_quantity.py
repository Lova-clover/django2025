# Generated by Django 5.1.1 on 2025-02-01 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_profile_crop_profile_produce_info_profile_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
