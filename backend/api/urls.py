from django.urls import path
from . import views
from rest_framework import routers, viewsets

router = routers.DefaultRouter()

router.register('catalog', views.CatalogViewSet, basename='catalog')

router.register('subscribe', views.SubscribeViewSet, basename='subscribe')

urlpatterns = [
]
urlpatterns += router.urls