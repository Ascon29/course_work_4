from django.forms import ModelForm

from newsletter.models import Recipient, Message, NewsLetter


class RecipientForm(ModelForm):
    class Meta:
        model = Recipient
        fields = '__all__'


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = '__all__'


class NewsletterForm(ModelForm):
    class Meta:
        model = NewsLetter
        fields = ['message', 'recipient']
