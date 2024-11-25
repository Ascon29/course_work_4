from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from django.views.decorators.cache import cache_page

from users.apps import UsersConfig
from users.views import (
    UserRegisterView,
    email_verification,
    UserListView,
    UserUpdateView,
    UserDetailView,
    BanUserView,
    UnbanUserView,
    UserProfileView,
    UserForgotPasswordView,
    UserPasswordResetConfirmView,
)

app_name = UsersConfig.name

urlpatterns = [
    path("login/", LoginView.as_view(template_name="users/login.html"), name="login"),
    path("logout/", LogoutView.as_view(next_page="/"), name="logout"),
    path(
        "register/",
        UserRegisterView.as_view(template_name="users/register.html"),
        name="register",
    ),
    path("email_confirm/<str:token>/", email_verification, name="email_confirm"),
    path("user_list/", UserListView.as_view(), name="user_list"),
    path("users/<int:pk>/update/", UserUpdateView.as_view(), name="user_update"),
    path(
        "users/<int:pk>/detail/",
        cache_page(10)(UserDetailView.as_view()),
        name="user_detail",
    ),
    path(
        "users/<int:pk>/user_profile/",
        cache_page(10)(UserProfileView.as_view(template_name="users/user_profile.html")),
        name="user_profile",
    ),
    path("ban_user/<int:pk>/", BanUserView.as_view(), name="ban_user"),
    path("unban_user/<int:pk>/", UnbanUserView.as_view(), name="unban_user"),
    path("password-reset/", UserForgotPasswordView.as_view(), name="password_reset"),
    path("set-new-password/<uidb64>/<token>/", UserPasswordResetConfirmView.as_view(), name="password_reset_confirm"),
]
