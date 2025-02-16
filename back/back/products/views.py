from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @action(detail=False, methods=['get'])
    def inventory_summary(self):
        """Retorna un resumen del inventario por categoría y marca"""
        summary = {}
        for category, _ in Product.CATEGORY_CHOICES:
            summary[category] = {
                'total': Product.objects.filter(category=category).count(),
                'by_brand': {}
            }
            brands = Product.objects.filter(category=category).values('brand').distinct()
            for brand in brands:
                brand_name = brand['brand']
                count = Product.objects.filter(category=category, brand=brand_name).count()
                summary[category]['by_brand'][brand_name] = count
        
        return Response(summary) 