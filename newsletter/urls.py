from django.urls import path
from django.views.decorators.cache import cache_page

from newsletter.apps import NewsletterConfig
from newsletter.views import (
    MainPage,
    RecipientListView,
    RecipientCreateView,
    RecipientDeleteView,
    RecipientUpdateView,
    RecipientDetailView,
    MessageListView,
    MessageCreateView,
    MessageDeleteView,
    MessageUpdateView,
    MessageDetailView,
    NewsletterListView,
    NewsletterCreateView,
    NewsletterDeleteView,
    NewsletterUpdateView,
    NewsletterDetailView,
    AttemptListView,
    start_newsletter,
    finish_newsletter,
)

app_name = NewsletterConfig.name

urlpatterns = [
    path("", cache_page(10)(MainPage.as_view()), name="main_page"),
    path("newsletter/recipient_list/", RecipientListView.as_view(), name="recipient_list"),
    path(
        "newsletter/recipient_create/",
        RecipientCreateView.as_view(),
        name="recipient_create",
    ),
    path(
        "newsletter/recipient_delete/<int:pk>/",
        RecipientDeleteView.as_view(),
        name="recipient_delete",
    ),
    path(
        "newsletter/recipient_update/<int:pk>/",
        RecipientUpdateView.as_view(),
        name="recipient_update",
    ),
    path(
        "newsletter/recipient_detail/<int:pk>/",
        cache_page(10)(RecipientDetailView.as_view()),
        name="recipient_detail",
    ),
    path("newsletter/message_list/", MessageListView.as_view(), name="message_list"),
    path("newsletter/message_create/", MessageCreateView.as_view(), name="message_create"),
    path(
        "newsletter/message_delete/<int:pk>/",
        MessageDeleteView.as_view(),
        name="message_delete",
    ),
    path(
        "newsletter/message_update/<int:pk>/",
        MessageUpdateView.as_view(),
        name="message_update",
    ),
    path(
        "newsletter/message_detail/<int:pk>/",
        cache_page(10)(MessageDetailView.as_view()),
        name="message_detail",
    ),
    path(
        "newsletter/newsletter_list/",
        NewsletterListView.as_view(),
        name="newsletter_list",
    ),
    path(
        "newsletter/newsletter_create/",
        NewsletterCreateView.as_view(),
        name="newsletter_create",
    ),
    path(
        "newsletter/newsletter_delete/<int:pk>/",
        NewsletterDeleteView.as_view(),
        name="newsletter_delete",
    ),
    path(
        "newsletter/newsletter_update/<int:pk>/",
        NewsletterUpdateView.as_view(),
        name="newsletter_update",
    ),
    path(
        "newsletter/newsletter_detail/<int:pk>/",
        cache_page(10)(NewsletterDetailView.as_view()),
        name="newsletter_detail",
    ),
    path("newsletter/attempt_list/", AttemptListView.as_view(), name="attempt_list"),
    path("finish_newsletter/<int:pk>/", finish_newsletter, name="finish_newsletter"),
    path("start_newsletter/<int:pk>/", start_newsletter, name="start_newsletter"),
]
