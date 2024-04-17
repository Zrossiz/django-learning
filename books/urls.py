from django.contrib import admin
from django.template.defaulttags import url
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from store.views import BookViewSet

router = SimpleRouter()

router.register(r'book', BookViewSet)

urlpatterns = [
    path('', include('main.urls')),
    path('admin/', admin.site.urls)
]

urlpatterns += router.urls
