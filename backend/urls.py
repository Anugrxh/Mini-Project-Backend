from django.urls import path, include
from accounts.views import CustomGoogleLogin
from accounts.views import SignupView, LoginView, LogoutView, VideoEmotionAnalysisView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('api/signup/', SignupView.as_view(), name='signup'),
    path('api/login/', LoginView.as_view(), name='login'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/logout/', LogoutView.as_view(), name='logout'),
    path('api/emotion-video/', VideoEmotionAnalysisView.as_view(), name='video_emotion'),

    # Custom Google login endpoint
    path('api/social/google/login/', CustomGoogleLogin.as_view(), name='google_login'),

    # Include dj-rest-auth default urls for regular auth and registration
    path('api/dj-rest-auth/', include('dj_rest_auth.urls')),
    path('api/dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('api/dj-rest-auth/social/', include('allauth.socialaccount.urls')),
]
