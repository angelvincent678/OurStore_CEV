# Generated by Django 5.1.1 on 2024-10-29 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adm', '0007_delete_sale'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='real_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
