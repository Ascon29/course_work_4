import secrets
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, ListView, DetailView, View
from django.contrib.messages.views import SuccessMessageMixin

from .forms import UserForgotPasswordForm, UserSetNewPasswordForm
from config import settings
from users.forms import UserRegisterForm, UserUpdateForm
from users.models import User


class UserRegisterView(CreateView):
    """Контроллер для регистрации пользователя. Отправляет пользователю письмо для верификации email адреса"""

    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f"http://{host}/users/email_confirm/{token}/"
        send_mail(
            subject="Подтверждение почты",
            message=f"Чтобы подтвердить почту, перейди по ссылке: {url}",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email],
        )
        return super().form_valid(form)


def email_verification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse("users:login"))


class UserListView(LoginRequiredMixin, ListView):
    """Контроллер отображения списка пользователей"""

    model = User

    def get_queryset(self):
        """Чтобы админ не видел себя в списке пользователей и случайно не забанил :)"""

        return User.objects.filter(is_staff=False)


class UserDetailView(LoginRequiredMixin, DetailView):
    """Контроллер отображения детальной информации о пользователе"""

    model = User


class UserUpdateView(LoginRequiredMixin, UpdateView):
    """Контроллер редактирования профиля пользователя"""

    model = User
    form_class = UserUpdateForm
    success_url = reverse_lazy("newsletter:main_page")


class UserProfileView(LoginRequiredMixin, DetailView):
    """Контроллер отображения профиля пользователя"""

    model = User


class BanUserView(LoginRequiredMixin, View):
    """Контроллер для блокировки пользователя"""

    def post(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        if not request.user.has_perm("can_ban_user"):
            return HttpResponseForbidden("У вас нет на это прав")
        user.is_active = False
        user.save()
        return redirect("users:user_detail", pk=pk)


class UnbanUserView(LoginRequiredMixin, View):
    """Контроллер для разблокировки пользователя"""

    def post(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        if not request.user.has_perm("can_ban_user"):
            return HttpResponseForbidden("У вас нет на это прав")
        user.is_active = True
        user.save()
        return redirect("users:user_detail", pk=pk)


class UserForgotPasswordView(SuccessMessageMixin, PasswordResetView):
    """
    Представление по сбросу пароля по почте
    """

    form_class = UserForgotPasswordForm
    template_name = "users/user_password_reset.html"
    success_url = reverse_lazy("newsletter:main_page")
    success_message = "Письмо с инструкцией по восстановлению пароля отправлена на ваш email"
    subject_template_name = "users/email/password_subject_reset_mail.txt"
    email_template_name = "users/email/password_reset_mail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Запрос на восстановление пароля"
        return context


class UserPasswordResetConfirmView(SuccessMessageMixin, PasswordResetConfirmView):
    """
    Представление установки нового пароля
    """

    form_class = UserSetNewPasswordForm
    template_name = "users/user_password_set_new.html"
    success_url = reverse_lazy("users:login")
    success_message = "Пароль успешно изменен. Можете авторизоваться на сайте."

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Установить новый пароль"
        return context
