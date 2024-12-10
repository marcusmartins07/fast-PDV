from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from .models import Produto, Categoria
from .serializers import ProdutoSerializer, CategoriaSerializer 
from rest_framework.permissions import IsAuthenticated

import time
import random
espera = random.randint(1, 5)
time.sleep(espera)
print(espera)

class ProdutoViewSet(mixins.CreateModelMixin, 
                      mixins.ListModelMixin, 
                      mixins.RetrieveModelMixin, 
                      mixins.UpdateModelMixin, 
                      mixins.DestroyModelMixin, 
                      viewsets.GenericViewSet):
    
    permission_classes = [IsAuthenticated]

    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

    @action(detail=False, methods=['get'])
    def buscar_por_codigo_barras(self, request):
        codigo_barras = request.query_params.get('codigo_barras', None)
        if codigo_barras:
            try:
                produto = self.queryset.get(codigo_barras=codigo_barras)
                serializer = self.get_serializer(produto)
                return Response(serializer.data)
            except Produto.DoesNotExist:
                return Response({"detail": "Produto não encontrado."}, status=status.HTTP_404_NOT_FOUND)
        return Response({"detail": "Código de barras não fornecido."}, status=status.HTTP_400_BAD_REQUEST)


class CategoriaViewSet(mixins.ListModelMixin,
                       mixins.CreateModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin,
                       viewsets.GenericViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
