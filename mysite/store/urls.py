from django.urls import path, include
from rest_framework import routers
from .views import (UserProfileAPIView, UserProfileSimpleAPIView, CountryViewSet, CityViewSet,
                    PropertyListAPIView, PropertyDetailAPIView,
                    BookingViewSet, RegisterView, LoginView, LogoutView,
                    ReviewViewSet, AmenityViewSet)

router = routers.DefaultRouter()
router.register(r'country', CountryViewSet)
router.register(r'city', CityViewSet)
router.register(r'booking', BookingViewSet)
router.register(r'review', ReviewViewSet)
router.register(r'amenities', AmenityViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('property/', PropertyListAPIView.as_view(), name='property_list'),
    path('property/<int:pk>/', PropertyDetailAPIView.as_view(), name='property_detail'),
    path('user/', UserProfileAPIView.as_view(), name='user_list'),
    path('user/<int:pk>/', UserProfileSimpleAPIView.as_view(), name='user_detail'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]