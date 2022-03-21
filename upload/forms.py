from django.forms import ModelForm
from .models import Upload


class CreateModelForm(ModelForm):
    class Meta:
        model = Upload
        fields = '__all__'
        exclude = ('uploader',)
