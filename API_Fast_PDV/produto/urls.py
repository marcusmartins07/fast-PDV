from django.urls import path
from .views import ProdutoViewSet, CategoriaViewSet
from rest_framework.routers import DefaultRouter


routerProduto = DefaultRouter()

routerProduto.register(r'produto', ProdutoViewSet)
routerProduto.register('categoria', CategoriaViewSet)
