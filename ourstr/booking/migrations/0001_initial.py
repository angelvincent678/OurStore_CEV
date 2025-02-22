# Generated by Django 5.1.1 on 2024-10-30 12:40

import booking.models
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('adm', '0009_product_reserved_quantity_alter_product_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('booking_start', models.DateTimeField(default=django.utils.timezone.now)),
                ('booking_end', models.DateTimeField(default=booking.models.get_default_booking_end)),
                ('confirmed', models.BooleanField(default=False)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adm.product')),
            ],
        ),
    ]
