from django.forms import ModelForm
from .models import MOHArea, Sample


class MOHAreaForm(ModelForm):
    class Meta:
        model = MOHArea
        fields = ["name", "district", "address", "phone", "email"]


class SampleForm(ModelForm):
    class Meta:
        model = Sample
        fields = "__all__"
