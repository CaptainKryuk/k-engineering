from django.urls import path
from django.views.generic import base
from . import views
from rest_framework import routers, viewsets

router = routers.DefaultRouter()

router.register('catalog', views.CatalogViewSet, basename='catalog')

router.register('subscribe', views.SubscribeViewSet, basename='subscribe')

router.register('order', views.OrderViewSet, basename='order')

router.register('material', views.MaterialViewSet, basename='material')

urlpatterns = [
  path('request/', views.request_view)
]
urlpatterns += router.urls