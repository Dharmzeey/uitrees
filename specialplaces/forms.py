from django.forms import ModelForm
from.models import SpecialPlace


class CreateSpecialForm(ModelForm):
    class Meta:
        model = SpecialPlace
        fields = "__all__"
        exclude = ('uploader',)
