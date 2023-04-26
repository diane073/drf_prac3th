from django.urls import path
from users import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('signup/', views.UserView.as_view(), name='signup'),
    path('mock/', views.mockView.as_view(), name = 'mock'),
    path('api/token/', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'), #토큰 지급, login
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), #토큰연장
]