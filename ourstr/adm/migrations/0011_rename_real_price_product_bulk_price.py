# Generated by Django 5.1.1 on 2024-10-31 10:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adm', '0010_rename_profile_customer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='real_price',
            new_name='bulk_price',
        ),
    ]
