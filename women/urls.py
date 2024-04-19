from django.urls import path

from women.views import *

urlpatterns = [
    path('api/womenlist/', WomenApiList.as_view()),
    path('api/womenlist/<int:pk>/', ...)
]