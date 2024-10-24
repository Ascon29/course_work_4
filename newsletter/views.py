from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from newsletter.models import Recipient, Message, NewsLetter


# Контроллеры CRUD для получателей ---------------------------------
class RecipientListView(ListView):
    model = Recipient


class RecipientDetailView(DetailView):
    model = Recipient


class RecipientCreateView(CreateView):
    model = Recipient
    fields = ('email', 'name', 'comment')
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
    fields = ('head', 'body')
    success_url = reverse_lazy('newsletter:message_list')


class MessageUpdateView(UpdateView):
    model = Message
    fields = ('head', 'body')
    success_url = reverse_lazy('newsletter:message_list')


class MessageDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy('newsletter:message_list')


# Контроллеры CRUD для рассылок ---------------------------------

class NewsLetterListView(ListView):
    model = NewsLetter


class NewsLetterDetailView(DetailView):
    model = NewsLetter


class NewsLetterCreateView(CreateView):
    model = NewsLetter
    fields = ('message', 'recipient')
    success_url = reverse_lazy('newsletter:newsletter_list')


class NewsLetterUpdateView(UpdateView):
    model = NewsLetter
    fields = ('message', 'recipient')
    success_url = reverse_lazy('newsletter:newsletter_list')


class NewsLetterDeleteView(DeleteView):
    model = NewsLetter
    fields = ('message', 'recipient')
    success_url = reverse_lazy('newsletter:newsletter_list')
