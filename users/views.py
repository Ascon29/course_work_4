import secrets

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, ListView, DetailView, View

from config import settings
from users.forms import UserRegisterForm, UserUpdateForm
from users.models import User


class UserRegisterView(CreateView):
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
    model = User


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    success_url = reverse_lazy("users:user_list")


class BanUserView(LoginRequiredMixin, View):

    def post(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        if not request.user.has_perm('can_ban_user'):
            return HttpResponseForbidden('У вас нет на это прав')
        user.is_active = False
        user.save()
        return redirect('users:user_detail', pk=pk)


class UnbanUserView(LoginRequiredMixin, View):

    def post(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        if not request.user.has_perm('can_ban_user'):
            return HttpResponseForbidden('У вас нет на это прав')
        user.is_active = True
        user.save()
        return redirect('users:user_detail', pk=pk)
