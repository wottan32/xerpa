# Generated by Django 5.0.6 on 2024-06-26 22:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TX', '0004_categorias_alter_comercios_merchant_logo_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Categorias',
            new_name='Category',
        ),
        migrations.RenameModel(
            old_name='Keywords',
            new_name='Keyword',
        ),
        migrations.RenameModel(
            old_name='Comercios',
            new_name='Merchant',
        ),
        migrations.RenameModel(
            old_name='Transacciones',
            new_name='Transaction',
        ),
    ]
