from django.forms import ModelForm
from .models import MOHArea


class MOHAreaForm(ModelForm):
    class Meta:
        model = MOHArea
        fields = ["name", "district", "address", "phone", "email"]
