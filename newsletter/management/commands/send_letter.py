from django.core.mail import send_mail
from django.core.management import BaseCommand

from config import settings


class Command(BaseCommand):
    def handle(self, *args, **options):
        head = input("Тема письма: ")
        body = input("Сообщение: ")
        recipient = input("Получатель (email): ")
        recipient_list = [recipient]
        from_email = settings.EMAIL_HOST_USER

        try:
            send_mail(head, body, from_email, recipient_list)
            print("Письмо успешно отправлено")
        except Exception as e:
            print(f"Произошла ошибка при отправке письма: {e}")
