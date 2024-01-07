from django.urls import path, include
from rest_framework import routers
from mercado_kids import views

router = routers.DefaultRouter()
router.register(r'client_papa', views.ClientePapaView, 'cliente_papa')
router.register(r'client_nino', views.ClienteNinoView, 'cliente_nino')

urlpatterns = [
    path('client_papa/search/', views.ClientePapaByName.as_view(), name='cliente_papa_by_nombre'),
    path('', include(router.urls))
]