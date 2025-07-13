from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from django.contrib.auth.views import LogoutView

from . import views
from . import frontend_views

router = DefaultRouter()
router.register(r'products', views.ProductViewSet)
router.register(r'reviews', views.ReviewViewSet)

urlpatterns = [
    # Authentication endpoints
    path('auth/register/', views.UserRegistrationView.as_view(), name='user-register'),
    path('auth/login/', views.UserLoginView.as_view(), name='user-login'),
    path('auth/logout/', views.UserLogoutView.as_view(), name='user-logout'),
    path('auth/token/', obtain_auth_token, name='api-token-auth'),
    
    # User profile
    path('auth/profile/', views.UserProfileView.as_view(), name='user-profile'),
    
    # API endpoints
    path('api/', include(router.urls)),

    # Frontend views
    path('', frontend_views.home_view, name='home'),
    path('products/', frontend_views.products_view, name='products'),
    path('products/<int:product_id>/', frontend_views.product_detail_view, name='product_detail'),
    path('products/<int:product_id>/review/', frontend_views.submit_review_view, name='submit_review'),
    
    # Authentication views
    path('login/', frontend_views.login_view, name='login'),
    path('register/', frontend_views.register_view, name='register'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('profile/', frontend_views.profile_view, name='profile'),
]
