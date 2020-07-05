from django.urls import path, include
from rest_framework.routers import DefaultRouter
from portfolio import views

# Create a router and register our viewsets with it.

router = DefaultRouter()

router.register('feedbacks', views.FeedbackViewSet)


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path('portfolio', views.get_portfolio),
]