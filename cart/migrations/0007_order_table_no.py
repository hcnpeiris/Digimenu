# Generated by Django 4.2.16 on 2024-10-09 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0006_rename_restaurant_order_resturant'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='table_no',
            field=models.PositiveBigIntegerField(default=1),
        ),
    ]