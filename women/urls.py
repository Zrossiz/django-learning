from django.urls import path, include
from women.views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'women', WomenViewSet)

urlpatterns = [
    path('api/', include(router.urls))
]