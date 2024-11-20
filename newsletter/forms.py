from django.forms import ModelForm

from newsletter.models import Recipient


class RecipientForm(ModelForm):
    class Meta:
        model = Recipient
        fields = '__all__'
