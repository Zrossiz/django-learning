from django.urls import path

from women.views import WomenApiView

urlpatterns = [
    path('api/womenlist/', WomenApiView.as_view()),
    path('api/womenlist/<int:pk>/', WomenApiView.as_view())
]