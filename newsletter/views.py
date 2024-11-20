from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from newsletter.forms import RecipientForm, MessageForm, NewsletterForm
from newsletter.models import Recipient, Message, NewsLetter


class MainPage(TemplateView):
    template_name = 'newsletter/main_page.html'


# Контроллеры CRUD для получателей ---------------------------------
class RecipientListView(ListView):
    model = Recipient


class RecipientDetailView(DetailView):
    model = Recipient


class RecipientCreateView(CreateView):
    model = Recipient
    form_class = RecipientForm
    success_url = reverse_lazy('newsletter:recipient_list')


class RecipientUpdateView(UpdateView):
    model = Recipient
    fields = ('email', 'name', 'comment')
    success_url = reverse_lazy('newsletter:recipient_list')


class RecipientDeleteView(DeleteView):
    model = Recipient
    success_url = reverse_lazy('newsletter:recipient_list')


# Контроллеры CRUD для сообщений ---------------------------------

class MessageListView(ListView):
    model = Message


class MessageDetailView(DetailView):
    model = Message


class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('newsletter:message_list')


class MessageUpdateView(UpdateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('newsletter:message_list')


class MessageDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy('newsletter:message_list')


# Контроллеры CRUD для рассылок ---------------------------------

class NewsletterListView(ListView):
    model = NewsLetter


class NewsletterDetailView(DetailView):
    model = NewsLetter


class NewsletterCreateView(CreateView):
    model = NewsLetter
    form_class = NewsletterForm
    success_url = reverse_lazy('newsletter:newsletter_list')


class NewsletterUpdateView(UpdateView):
    model = NewsLetter
    form_class = NewsletterForm
    success_url = reverse_lazy('newsletter:newsletter_list')


class NewsletterDeleteView(DeleteView):
    model = NewsLetter
    success_url = reverse_lazy('newsletter:newsletter_list')
