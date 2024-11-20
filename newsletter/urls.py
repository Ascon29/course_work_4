from django.urls import path
from newsletter.apps import NewsletterConfig
from newsletter.views import MainPage, RecipientListView, RecipientCreateView, RecipientDeleteView, RecipientUpdateView, \
    RecipientDetailView, MessageListView, MessageCreateView, MessageDeleteView, MessageUpdateView, MessageDetailView

app_name = NewsletterConfig.name

urlpatterns = [
    path('', MainPage.as_view(), name='main_page'),
    path('newsletter/recipient_list/', RecipientListView.as_view(), name='recipient_list'),
    path('newsletter/recipient_create/', RecipientCreateView.as_view(), name='recipient_create'),
    path('newsletter/recipient_delete/<int:pk>/', RecipientDeleteView.as_view(), name='recipient_delete'),
    path('newsletter/recipient_update/<int:pk>/', RecipientUpdateView.as_view(), name='recipient_update'),
    path('newsletter/recipient_detail/<int:pk>/', RecipientDetailView.as_view(), name='recipient_detail'),

    path('newsletter/message_list/', MessageListView.as_view(), name='message_list'),
    path('newsletter/message_create/', MessageCreateView.as_view(), name='message_create'),
    path('newsletter/message_delete/<int:pk>/', MessageDeleteView.as_view(), name='message_delete'),
    path('newsletter/message_update/<int:pk>/', MessageUpdateView.as_view(), name='message_update'),
    path('newsletter/message_detail/<int:pk>/', MessageDetailView.as_view(), name='message_detail'),
]
