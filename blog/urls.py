from django.urls import path, include
from . import views
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView,)

router = routers.DefaultRouter()
router.register('posts', views.PostView)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls))
]
