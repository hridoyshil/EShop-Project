# Generated by Django 4.2.4 on 2023-08-17 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_rename_data_order_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]