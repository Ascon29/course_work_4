from django.core.management import BaseCommand
from django.contrib.auth.models import Group, Permission


class Command(BaseCommand):
    """Команда для создания группы Менеджеров через консоль"""

    def handle(self, *args, **options):
        managers = Group.objects.create(name="managers")
        view_users = Permission.objects.get(codename="view_user")
        view_newsletter = Permission.objects.get(codename="view_newsletter")
        view_recipient = Permission.objects.get(codename="view_recipient")
        view_message = Permission.objects.get(codename="view_message")
        view_attempt = Permission.objects.get(codename="view_attempt")
        can_ban_users = Permission.objects.get(codename="can_ban_user")
        can_stop_newsletter = Permission.objects.get(codename="can_stop_newsletter")
        managers.permissions.add(
            view_users,
            view_newsletter,
            view_recipient,
            view_message,
            view_attempt,
            can_ban_users,
            can_stop_newsletter,
        )
