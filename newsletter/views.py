from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.mail import send_mail
from django.http import HttpResponseForbidden
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView,
)

from config import settings
from newsletter.forms import RecipientForm, MessageForm, NewsletterForm
from newsletter.models import Recipient, Message, NewsLetter, Attempt
from newsletter.services import (
    get_recipients_from_cache,
    get_newsletters_from_cache,
    get_messages_from_cache,
    get_attempts_from_cache,
)
from users.models import User


class MainPage(TemplateView):
    """Контроллер отображения главной страницы"""

    models = [Recipient, NewsLetter]
    template_name = "newsletter/main_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["recipient_all"] = Recipient.objects.all()
        context["newsletter_all"] = NewsLetter.objects.all()
        context["newsletter_active"] = NewsLetter.objects.filter(status=NewsLetter.START)
        return context


# Контроллеры CRUD для получателей ---------------------------------
class RecipientListView(LoginRequiredMixin, ListView):
    model = Recipient

    def get_queryset(self):
        if self.request.user.has_perm("newsletter.view_recipient"):
            return get_recipients_from_cache()
        return get_recipients_from_cache().filter(owner=self.request.user)


class RecipientDetailView(LoginRequiredMixin, DetailView):
    model = Recipient


class RecipientCreateView(LoginRequiredMixin, CreateView):
    model = Recipient
    form_class = RecipientForm
    success_url = reverse_lazy("newsletter:recipient_list")

    def form_valid(self, form):
        recipient = form.save()
        user = self.request.user
        recipient.owner = user
        recipient.save()
        return super().form_valid(form)


class RecipientUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Recipient
    fields = ("email", "name", "comment")
    success_url = reverse_lazy("newsletter:recipient_list")

    def test_func(self):
        recipient = self.get_object()
        return self.request.user == recipient.owner

    def handle_no_permission(self):
        return HttpResponseForbidden("У вас нет на это прав")

    def get_success_url(self):
        return reverse_lazy("newsletter:recipient_detail", kwargs={"pk": self.object.pk})


class RecipientDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Recipient
    success_url = reverse_lazy("newsletter:recipient_list")

    def test_func(self):
        recipient = self.get_object()
        return self.request.user == recipient.owner

    def handle_no_permission(self):
        return HttpResponseForbidden("У вас нет на это прав")


# Контроллеры CRUD для сообщений ---------------------------------


class MessageListView(LoginRequiredMixin, ListView):
    model = Message

    def get_queryset(self):
        if self.request.user.has_perm("newsletter.view_message"):
            return get_messages_from_cache()
        return get_messages_from_cache().filter(owner=self.request.user)


class MessageDetailView(LoginRequiredMixin, DetailView):
    model = Message


class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy("newsletter:message_list")

    def form_valid(self, form):
        message = form.save()
        user = self.request.user
        message.owner = user
        message.save()
        return super().form_valid(form)


class MessageUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy("newsletter:message_list")

    def test_func(self):
        message = self.get_object()
        return self.request.user == message.owner

    def handle_no_permission(self):
        return HttpResponseForbidden("У вас нет на это прав")

    def get_success_url(self):
        return reverse_lazy("newsletter:message_detail", kwargs={"pk": self.object.pk})


class MessageDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Message
    success_url = reverse_lazy("newsletter:message_list")

    def test_func(self):
        message = self.get_object()
        return self.request.user == message.owner

    def handle_no_permission(self):
        return HttpResponseForbidden("У вас нет на это прав")


# Контроллеры CRUD для рассылок ---------------------------------


class NewsletterListView(LoginRequiredMixin, ListView):
    model = NewsLetter

    def get_queryset(self):
        if self.request.user.has_perm("newsletter.view_newsletter"):
            return get_newsletters_from_cache()
        return get_newsletters_from_cache().filter(owner=self.request.user)


class NewsletterDetailView(LoginRequiredMixin, DetailView):
    model = NewsLetter


class NewsletterCreateView(LoginRequiredMixin, CreateView):
    model = NewsLetter
    form_class = NewsletterForm
    success_url = reverse_lazy("newsletter:newsletter_list")

    def form_valid(self, form):
        newsletter = form.save()
        user = self.request.user
        newsletter.owner = user
        newsletter.save()
        return super().form_valid(form)


class NewsletterUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = NewsLetter
    form_class = NewsletterForm
    success_url = reverse_lazy("newsletter:newsletter_list")

    def test_func(self):
        newsletter = self.get_object()
        return self.request.user == newsletter.owner

    def handle_no_permission(self):
        return HttpResponseForbidden("У вас нет на это прав")

    def get_success_url(self):
        return reverse_lazy("newsletter:newsletter_detail", kwargs={"pk": self.object.pk})


class NewsletterDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = NewsLetter
    success_url = reverse_lazy("newsletter:newsletter_list")

    def test_func(self):
        newsletter = self.get_object()
        return self.request.user == newsletter.owner

    def handle_no_permission(self):
        return HttpResponseForbidden("У вас нет на это прав")


class AttemptListView(LoginRequiredMixin, ListView):
    """Контроллер отображения списка попыток рассылок"""

    model = Attempt
    template_name = "newsletter/attempt_list.html"

    def get_queryset(self):
        if self.request.user.has_perm("newsletter.view_attempt"):
            return get_attempts_from_cache()
        return get_attempts_from_cache().filter(owner=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        attempt = self.get_queryset()
        context["success"] = attempt.filter(status="Успешно")
        context["not_success"] = attempt.filter(status="Не успешно")
        context["all"] = attempt
        return context


def finish_newsletter(request, pk):
    """Контроллер для завершения рассылки.
    Проверяет на наличие прав как для владельца, так и для менеджера"""

    newsletter = NewsLetter.objects.get(pk=pk)
    user = User.objects.get(id=request.user.id)
    if not request.user.has_perm("newsletter.can_stop_newsletter") and newsletter.owner != user:
        return HttpResponseForbidden("У вас нет на это прав")
    newsletter.status = NewsLetter.END
    newsletter.date_of_end_shipment = datetime.now()
    newsletter.save()
    return redirect("newsletter:newsletter_detail", pk=pk)


def start_newsletter(request, pk):
    """Контроллер запуска рассылки"""

    newsletter = NewsLetter.objects.get(pk=pk)
    subject = newsletter.message.head
    message = newsletter.message.body
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [recipient.email for recipient in newsletter.recipient.all()]
    owner = newsletter.owner
    for recipient in recipient_list:
        try:
            send_mail(
                subject,
                message,
                from_email,
                [recipient],
            )
            newsletter.status = NewsLetter.START
            newsletter.date_of_end_shipment = None
            newsletter.date_of_first_shipment = datetime.now()
            newsletter.save()

            attempt = Attempt(
                date_of_attempt=datetime.now(),
                status=Attempt.SUCCESS,
                mail_server_response=f"Сообщение успешно отправлено получателю: {recipient}",
                newsletter=newsletter,
                owner=owner,
            )
            attempt.save()

        except Exception as e:
            newsletter.status = NewsLetter.START
            newsletter.date_of_end_shipment = None
            newsletter.date_of_first_shipment = datetime.now()
            newsletter.save()

            attempt = Attempt(
                date_of_attempt=datetime.now(),
                status=Attempt.NOT_SUCCESS,
                mail_server_response=f"При отправке сообщения произошла ошибка: {e}",
                newsletter=newsletter,
                owner=owner,
            )
            attempt.save()

    return redirect("newsletter:newsletter_detail", pk=pk)
