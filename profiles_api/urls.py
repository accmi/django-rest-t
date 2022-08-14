from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import hello_api_view, HelloViewSet

router = DefaultRouter()

router.register('hello-viewset', HelloViewSet, base_name='hello-viewset')

urlpatterns = [
    path('hello-view/', hello_api_view),
    path('', include(router.urls))
]

