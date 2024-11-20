from django.urls import path
from newsletter.apps import NewsletterConfig
from newsletter.views import MainPage, RecipientListView, RecipientCreateView, RecipientDeleteView, RecipientUpdateView, \
    RecipientDetailView

app_name = NewsletterConfig.name

urlpatterns = [
    path('', MainPage.as_view(), name='main_page'),
    path('newsletter/recipient_list/', RecipientListView.as_view(), name='recipient_list'),
    path('newsletter/recipient_create/', RecipientCreateView.as_view(), name='recipient_create'),
    path('newsletter/recipient_delete/<int:pk>/', RecipientDeleteView.as_view(), name='recipient_delete'),
    path('newsletter/recipient_update/<int:pk>/', RecipientUpdateView.as_view(), name='recipient_update'),
    path('newsletter/recipient_detail/<int:pk>/', RecipientDetailView.as_view(), name='recipient_detail'),
]
