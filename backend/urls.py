from django.urls import path
from accounts.views import SignupView, LoginView, LogoutView,VideoEmotionAnalysisView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('api/signup/', SignupView.as_view(), name='signup'),
    path('api/login/', LoginView.as_view(), name='login'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/logout/', LogoutView.as_view(), name='logout'),
    path('api/emotion-video/', VideoEmotionAnalysisView.as_view(), name='video_emotion'),
]
