# Generated by Django 5.0.6 on 2024-06-26 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TX', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(db_index=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='category',
            name='type',
            field=models.CharField(db_index=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='keyword',
            name='keyword',
            field=models.CharField(db_index=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='merchant',
            name='merchant_name',
            field=models.CharField(db_index=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='date',
            field=models.DateField(db_index=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='description',
            field=models.CharField(db_index=True, max_length=200),
        ),
    ]
