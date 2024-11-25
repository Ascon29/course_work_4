from django.core.cache import cache

from config.settings import CACHE_ENABLED
from newsletter.models import Recipient, Message, NewsLetter, Attempt


def get_recipients_from_cache():
    """Функция кэширования списка пользователей"""

    if not CACHE_ENABLED:
        return Recipient.objects.all()
    key = "recipient_list"
    recipients = cache.get(key)
    if recipients is not None:
        return recipients
    recipients = Recipient.objects.all()
    cache.set(key, recipients, 10)
    return recipients


def get_messages_from_cache():
    """Функция кэширования списка сообщений"""

    if not CACHE_ENABLED:
        return Message.objects.all()
    key = "message_list"
    messages = cache.get(key)
    if messages is not None:
        return messages
    messages = Message.objects.all()
    cache.set(key, messages, 10)
    return messages


def get_newsletters_from_cache():
    """Функция кэширования списка рассылок"""

    if not CACHE_ENABLED:
        return NewsLetter.objects.all()
    key = "newsletter_list"
    newsletters = cache.get(key)
    if newsletters is not None:
        return newsletters
    newsletters = NewsLetter.objects.all()
    cache.set(key, newsletters, 10)
    return newsletters


def get_attempts_from_cache():
    """Функция кэширования списка попыток рассылок"""

    if not CACHE_ENABLED:
        return Attempt.objects.all()
    key = "attempt_list"
    attempts = cache.get(key)
    if attempts is not None:
        return attempts
    attempts = Attempt.objects.all()
    cache.set(key, attempts, 10)
    return attempts
