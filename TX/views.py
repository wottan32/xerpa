from rest_framework import generics
from .models import Categorias, Comercios, Keywords, Transacciones
from .serializers import CategorySerializer, MerchantSerializer, KeywordSerializer, TransactionSerializer
from django.core.cache import cache
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


class protectedView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({'message': 'You are authenticated'}, status=status.HTTP_200_OK)


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class CategoryListCreate(generics.ListCreateAPIView):
    queryset = Categorias.objects.all()
    serializer_class = CategorySerializer


class CategoryRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categorias.objects.all()
    serializer_class = CategorySerializer


class MerchantListCreate(generics.ListCreateAPIView):
    queryset = Comercios.objects.all()
    serializer_class = MerchantSerializer


class MerchantRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comercios.objects.all()
    serializer_class = MerchantSerializer


class KeywordListCreate(generics.ListCreateAPIView):
    queryset = Keywords.objects.all()
    serializer_class = KeywordSerializer


class KeywordRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Keywords.objects.all()
    serializer_class = KeywordSerializer


class TransactionListCreate(generics.ListCreateAPIView):
    queryset = Transacciones.objects.all()
    serializer_class = TransactionSerializer


class TransactionRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transacciones.objects.all()
    serializer_class = TransactionSerializer


class EnrichTransactions(APIView):
    def post(self, request, *args, **kwargs):
        transactions_data = request.data
        enriched_transactions = []

        # Intenta recuperar los keywords de la caché
        keywords = cache.get('keywords')
        if not keywords:
            keywords = Keywords.objects.select_related('merchant', 'merchant__category').all()
            cache.set('keywords', keywords, timeout=60 * 15)  # Cache por 15 minutos

        keyword_dict = {keyword.keyword.lower(): keyword for keyword in keywords}

        for transaction_data in transactions_data:
            description = transaction_data.get('description', '').lower()
            amount = transaction_data.get('amount', None)
            date = transaction_data.get('date', None)

            enriched_transaction = {
                "description": description,
                "amount": amount,
                "date": date,
                "merchant": None,
                "category": None
            }

            if amount is None or date is None:
                return Response(
                    {"amount": ["This field is required."], "date": ["This field is required."]},
                    status=status.HTTP_400_BAD_REQUEST
                )

            merchant_found = False

            # Primer intento de enriquecimiento usando keywords
            for keyword, keyword_obj in keyword_dict.items():
                if keyword in description:
                    merchant = keyword_obj.merchant
                    category = merchant.category
                    enriched_transaction['merchant'] = {
                        "merchant_name": merchant.merchant_name,
                        "merchant_logo": merchant.merchant_logo
                    }
                    enriched_transaction['category'] = {
                        "name": category.name,
                        "type": category.type
                    }
                    merchant_found = True
                    break

            # Capa adicional de enriquecimiento
            if not merchant_found:
                merchant, category = self.additional_enrichment(description)
                if merchant:
                    enriched_transaction['merchant'] = {
                        "merchant_name": merchant.merchant_name,
                        "merchant_logo": merchant.merchant_logo
                    }
                if category:
                    enriched_transaction['category'] = {
                        "name": category.name,
                        "type": category.type
                    }

            enriched_transactions.append(enriched_transaction)

        return Response(enriched_transactions, status=status.HTTP_200_OK)

    def additional_enrichment(self, description):
        # Implementar lógica de enriquecimiento adicional
        # Esta lógica puede usar patrones comunes en descripciones y una base de datos de referencia ampliada
        # Aquí se proporciona un ejemplo básico
        common_patterns = {
            "supermercado": ("Supermercado Genérico", "Alimentos"),
            "restaurante": ("Restaurante Genérico", "Comida"),
            "uber": ("Uber", "Transporte"),
            "amazon": ("Amazon", "Compras")
        }

        for pattern, (merchant_name, category_name) in common_patterns.items():
            if pattern in description:
                merchant = Comercios.objects.filter(merchant_name=merchant_name).first()
                category = Categorias.objects.filter(name=category_name).first()
                return merchant, category

        return None, None
