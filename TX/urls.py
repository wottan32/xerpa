from django.urls import path
from .views import (
    CategoryListCreate, CategoryRetrieveUpdateDestroy,
    MerchantListCreate, MerchantRetrieveUpdateDestroy,
    KeywordListCreate, KeywordRetrieveUpdateDestroy,
    TransactionListCreate, TransactionRetrieveUpdateDestroy,
    EnrichTransactions, UserCreate
)

urlpatterns = [
    path('categorias/', CategoryListCreate.as_view(), name='category-list-create'),
    path('categorias/<uuid:pk>/', CategoryRetrieveUpdateDestroy.as_view(), name='category-retrieve-update-destroy'),
    path('comercios/', MerchantListCreate.as_view(), name='merchant-list-create'),
    path('comercios/<uuid:pk>/', MerchantRetrieveUpdateDestroy.as_view(), name='merchant-retrieve-update-destroy'),
    path('keywords/', KeywordListCreate.as_view(), name='keyword-list-create'),
    path('keywords/<uuid:pk>/', KeywordRetrieveUpdateDestroy.as_view(), name='keyword-retrieve-update-destroy'),
    path('transacciones/', TransactionListCreate.as_view(), name='transaction-list-create'),
    path('transacciones/<uuid:pk>/', TransactionRetrieveUpdateDestroy.as_view(), name='transaction-retrieve-update'
                                                                                      '-destroy'),
    path('enrich-transactions/', EnrichTransactions.as_view(), name='enrich-transactions'),
    path('register/', UserCreate.as_view(), name='user-create'),
]
