from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'categories', views.CategoryViewSet)
router.register(r'products', views.ProductViewSet)
router.register(r'orders', views.OrderViewSet, basename='order')
router.register(r'cart', views.CartViewSet, basename='cart')
router.register(r'cart-items', views.CartItemViewSet, basename='cart-item')
router.register(r'reviews', views.ReviewViewSet)
router.register(r'profile', views.UserProfileViewSet, basename='profile')
router.register(r'wishlist', views.WishlistViewSet, basename='wishlist')
router.register(r'coupons', views.CouponViewSet)

urlpatterns = [
    path('', include(router.urls)),
] 