import uuid
from django.db import models


class Categorias(models.Model):
    INCOME = 'income'
    EXPENSE = 'expense'
    TYPE_CHOICES = [
        (INCOME, 'Income'),
        (EXPENSE, 'Expense'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=50, choices=TYPE_CHOICES, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.name


class Comercios(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    merchant_name = models.CharField(max_length=255, blank=True, null=True)
    merchant_logo = models.CharField(max_length=255, blank=True, null=True)
    category = models.ForeignKey(Categorias, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.merchant_name


class Keywords(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    keyword = models.CharField(max_length=255, blank=True, null=True)
    merchant = models.ForeignKey(Comercios, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.keyword


class Transacciones(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.CharField(max_length=200, db_index=True, blank=True, null=True)
    amount = models.FloatField(null=True, blank=True)
    date = models.DateField(db_index=True, null=True, blank=True)
    merchant = models.ForeignKey(Comercios, null=True, blank=True, on_delete=models.SET_NULL)
    category = models.ForeignKey(Categorias, null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.amount is not None:
            if self.amount >= 0:
                self.category = Categorias.objects.get(type='income')
            else:
                self.category = Categorias.objects.get(type='expense')
        super().save(*args, **kwargs)

    def __str__(self):
        return self.description
