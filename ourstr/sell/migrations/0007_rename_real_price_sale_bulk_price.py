# Generated by Django 5.1.1 on 2024-10-31 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sell', '0006_alter_sale_product_price_alter_sale_real_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sale',
            old_name='real_price',
            new_name='bulk_price',
        ),
    ]
