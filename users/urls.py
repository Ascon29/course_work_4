from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from users.apps import UsersConfig
from users.views import UserRegisterView, email_verification

app_name = UsersConfig.name

urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path("logout/", LogoutView.as_view(next_page="/"), name="logout"),
    path("register/", UserRegisterView.as_view(), name="register"),
    path('email_confirm/<str:token>/', email_verification, name='email_confirm'),
]
