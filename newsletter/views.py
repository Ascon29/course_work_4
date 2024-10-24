from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from newsletter.models import Recipient, Message, NewsLetter


# Контроллеры CRUD для получателей ---------------------------------
class RecipientListView(ListView):
    model = Recipient


class RecipientDetailView(ListView):
    model = Recipient


class RecipientCreateView(ListView):
    model = Recipient
    fields = ('email', 'name', 'comment')
    success_url = reverse_lazy('newsletter:recipient_list')


class RecipientUpdateView(ListView):
    model = Recipient
    fields = ('email', 'name', 'comment')
    success_url = reverse_lazy('newsletter:recipient_list')


class RecipientDeleteView(ListView):
    model = Recipient
    success_url = reverse_lazy('newsletter:recipient_list')


# Контроллеры CRUD для сообщений ---------------------------------

class MessageListView(ListView):
    model = Message


class MessageDetailView(ListView):
    model = Message


class MessageCreateView(ListView):
    model = Message
    fields = ('head', 'body')
    success_url = reverse_lazy('newsletter:message_list')


class MessageUpdateView(ListView):
    model = Message
    fields = ('head', 'body')
    success_url = reverse_lazy('newsletter:message_list')


class MessageDeleteView(ListView):
    model = Message
    success_url = reverse_lazy('newsletter:message_list')


# Контроллеры CRUD для рассылок ---------------------------------

class NewsLetterListView(ListView):
    model = NewsLetter


class NewsLetterDetailView(ListView):
    model = NewsLetter


class NewsLetterCreateView(ListView):
    model = NewsLetter
    fields = ('message', 'recipient')
    success_url = reverse_lazy('newsletter:newsletter_list')


class NewsLetterUpdateView(ListView):
    model = NewsLetter
    fields = ('message', 'recipient')
    success_url = reverse_lazy('newsletter:newsletter_list')


class NewsLetterDeleteView(ListView):
    model = NewsLetter
    fields = ('message', 'recipient')
    success_url = reverse_lazy('newsletter:newsletter_list')
