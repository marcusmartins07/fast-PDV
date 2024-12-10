from django.urls import path
from .views import ClienteViewSet, EstadoViewSet, GeneroViewSet, UsuariosViewSet
from rest_framework.routers import SimpleRouter
from rest_framework.routers import DefaultRouter

routerUsuarios = SimpleRouter()
routerUsuarios.register('clientes', ClienteViewSet)
routerUsuarios.register('estados', EstadoViewSet)
routerUsuarios.register('generos', GeneroViewSet)


routerUsuarioLogado = DefaultRouter()
routerUsuarioLogado.register(r'usuarios', UsuariosViewSet)


