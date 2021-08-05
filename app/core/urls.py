from django.urls import path
from .views import CreateUserView, CreateTokenView, UsuarioLatLngView

urlpatterns = [
    path('v1/user/create/', CreateUserView.as_view(), name='create'),
    path('v1/user/token/', CreateTokenView.as_view(), name='token'),
    path('v1/user/ltn_lng/', UsuarioLatLngView.as_view(), name='latlng'),
]
