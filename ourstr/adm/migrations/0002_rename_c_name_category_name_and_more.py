# Generated by Django 5.1.1 on 2024-09-19 14:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adm', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='c_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='p_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='supplier',
            old_name='s_name',
            new_name='name',
        ),
    ]
