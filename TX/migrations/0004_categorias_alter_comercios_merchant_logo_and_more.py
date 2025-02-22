# Generated by Django 5.0.6 on 2024-06-26 22:00

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TX', '0003_rename_category_categorías_rename_merchant_comercios_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('type', models.CharField(choices=[('income', 'Income'), ('expense', 'Expense')], max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='comercios',
            name='merchant_logo',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='comercios',
            name='merchant_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='keywords',
            name='keyword',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='comercios',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TX.categorias'),
        ),
        migrations.AlterField(
            model_name='transacciones',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='TX.categorias'),
        ),
        migrations.DeleteModel(
            name='Categorías',
        ),
    ]
