from django.forms import ModelForm, BooleanField

from newsletter.models import Recipient, Message, NewsLetter


class StyleForm:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs["class"] = "form-check-input"
            else:
                field.widget.attrs["class"] = "form-control"


class RecipientForm(StyleForm, ModelForm):
    class Meta:
        model = Recipient
        fields = '__all__'


class MessageForm(StyleForm, ModelForm):
    class Meta:
        model = Message
        fields = '__all__'


class NewsletterForm(StyleForm, ModelForm):
    class Meta:
        model = NewsLetter
        fields = ['message', 'recipient']
