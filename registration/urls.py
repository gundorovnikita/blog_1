from django.urls import path

from . import views
app_name = 'users'

urlpatterns = [
    path('login/', views.AuthLoginView.as_view(), name="login"),
    path('signup/', views.AuthSignupView.as_view(), name="signup"),
    path('logout/', views.AuthLogoutView.as_view(), name="logout"),
]
