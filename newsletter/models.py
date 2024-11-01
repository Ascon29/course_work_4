from django.db import models


# Модель «Получатель рассылки»
class Recipient(models.Model):
    email = models.EmailField(unique=True, verbose_name="Email", help_text="Введите Email")
    name = models.CharField(max_length=100, verbose_name="Фамилия Имя Отчество", help_text='Введите Ф.И.О.')
    comment = models.TextField(verbose_name='Комментарий', blank=True, null=True, help_text='Введите комментарий')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['name']


# Модель «Сообщение»
class Message(models.Model):
    head = models.CharField(max_length=255, verbose_name='Тема письма', help_text='Введите тему письма')
    body = models.TextField(verbose_name='Сообщение', help_text='Введите сообщение')

    def __str__(self):
        return self.head

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
        ordering = ['head']


# Модель «Рассылка»
class NewsLetter(models.Model):
    STATUS_CHOICES = (
        ('end', 'Завершена'), ('created', 'Создана'), ('start', 'Запущена')
    )

    date_of_first_shipment = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время начала рассылки')
    date_of_end_shipment = models.DateTimeField(auto_now=True, verbose_name='Дата и время окончания рассылки')
    status = models.CharField(choices=STATUS_CHOICES, default='created', verbose_name='Статус рассылки')
    message = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name='Сообщение')
    recipient = models.ManyToManyField(Recipient, verbose_name='Получатель')

    def __str__(self):
        return self.status

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'
        ordering = ['status']


# Модель «Попытка рассылки»
class Attempt(models.Model):
    STATUS_CHOICES = (
        ('successful', 'Успешно'), ('not successful', 'Не успешно')
    )

    date_of_attempt = models.DateTimeField(auto_now=True, verbose_name='Дата и время попытки рассылки')
    status = models.CharField(choices=STATUS_CHOICES, default='created', verbose_name='Статус попытки рассылки')
    mail_server_response = models.TextField(verbose_name='Ответ почтового сервера')
    newsletter = models.ForeignKey(NewsLetter, on_delete=models.CASCADE, verbose_name='Рассылка')

    def __str__(self):
        return self.status

    class Meta:
        verbose_name = 'Попытка рассылки'
        verbose_name_plural = 'Попытки рассылки'
        ordering = ['status']
