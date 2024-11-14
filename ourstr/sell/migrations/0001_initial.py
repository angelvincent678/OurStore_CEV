# Generated by Django 5.1.1 on 2024-10-15 13:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('adm', '0007_delete_sale'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity_sold', models.IntegerField()),
                ('sell_date', models.DateTimeField(auto_now_add=True)),
                ('customer_name', models.CharField(max_length=55)),
                ('payment_method', models.CharField(max_length=55)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adm.product')),
            ],
        ),
    ]
