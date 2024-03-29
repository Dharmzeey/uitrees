from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib import messages

from utilities.mixins import AdminRequiredMixin
from utilities.location_validator import validate_location

from .models import SpecialPlace
from .forms import UploadSpecialPlaceForm
# Create your views here.


class Special(View):
    template_name = 'specialplaces/specialplaces.html'

    def get(self, request):
        places = SpecialPlace.objects.all()
        context = {
            'places': places
        }

        return render(request, self.template_name, context)


class SpecialDetails(View):
    template_name = 'specialplaces/specialplaces-detail.html'

    def get(self, request, pk):
        place = SpecialPlace.objects.get(id=pk)
        context = {
            'place': place,
            'pictures': [place.tree_picture, place.tree_picture2, place.tree_picture3]
        }

        return render(request, self.template_name, context)


class CreateSpecial(AdminRequiredMixin, CreateView):
    form_class = UploadSpecialPlaceForm
    success_url = reverse_lazy('special:special')
    template_name = 'specialplaces/specialplace-form.html'

    def form_valid(self, form):
        form.instance.uploader = self.request.user
        lat = form.instance.latitude
        long = form.instance.longitude
        check = validate_location(long, lat)
        if check == False:
            messages.error(self.request, "Sorry, You can not upload outside University of Ibadan")
            return render(self.request, self.template_name, {'form': form})
        else:
            form.save()
            messages.success(self.request, "Uploaded Successfully")
            return super(CreateSpecial, self).form_valid(form)
