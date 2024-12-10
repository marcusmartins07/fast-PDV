from django.contrib import admin
from django.urls import path, include
from usuarios.urls import routerUsuarios
from usuarios.urls import routerUsuarioLogado
from produto.urls import routerProduto
from pedido.urls import routerPedido
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/', include(routerProduto.urls)),
    path('api/v1/', include(routerUsuarios.urls)),
    path('api/v1/', include(routerUsuarioLogado.urls)),
    path('api/v1/', include(routerPedido.urls)),
    path('admin/', admin.site.urls),
    path('admin/', include('rest_framework.urls')),
]


