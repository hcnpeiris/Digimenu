# Generated by Django 4.2.16 on 2024-10-24 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0007_order_table_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='approval',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]