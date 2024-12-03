from django.forms import ModelForm, BooleanField

from newsletter.models import Recipient, Message, NewsLetter


class StyleForm:
    """Класс миксин для подключения стилей"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs["class"] = "form-check-input"
            else:
                field.widget.attrs["class"] = "form-control"


class RecipientForm(StyleForm, ModelForm):
    """Форма для создания получателя"""

    class Meta:
        model = Recipient
        exclude = ["owner"]


class MessageForm(StyleForm, ModelForm):
    """Форма для создания сообщения"""

    class Meta:
        model = Message
        exclude = ["owner"]


class NewsletterForm(StyleForm, ModelForm):
    """Форма для создания рассылки"""

    class Meta:
        model = NewsLetter
        exclude = ["owner", "status"]
