from django.forms import ModelForm
from .models import Upload


class UploadTreeForm(ModelForm):
    class Meta:
        model = Upload
        fields = '__all__'
        exclude = ('uploaded_by', 'requested_by')
