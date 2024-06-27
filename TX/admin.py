# admin.py
from django.contrib import admin
from .models import Categorias, Comercios, Keywords, Transacciones

admin.site.register(Categorias)
admin.site.register(Comercios)
admin.site.register(Keywords)
admin.site.register(Transacciones)
