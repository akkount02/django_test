from rest_framework.viewsets import ModelViewSet

import core.models as models
import api.serializers as serializers


class ProductModelView(ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
