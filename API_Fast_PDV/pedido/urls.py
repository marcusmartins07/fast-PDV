from django.urls import path
from .views import FormaPagamentoViewSet, PedidoViewSet
from rest_framework.routers import SimpleRouter


routerPedido = SimpleRouter()
routerPedido.register('formas_pagamento', FormaPagamentoViewSet)
routerPedido.register('pedido', PedidoViewSet)
