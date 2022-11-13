from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from .models import SpecialPlace
from .forms import CreateSpecialForm
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
    template_name = 'specialplaces/specialplaces_detail.html'

    def get(self, request, pk):
        place = SpecialPlace.objects.get(id=pk)
        context = {
            'place': place,
            'pictures': [place.tree_picture, place.tree_picture2, place.tree_picture3]
        }

        return render(request, self.template_name, context)


class CreateSpecial(LoginRequiredMixin, CreateView):
    form_class = CreateSpecialForm
    success_url = reverse_lazy('special:special')
    template_name = 'specialplaces/specialplace_form.html'

    def form_valid(self, form):
        form.instance.uploader = self.request.user
        messages.success(self.request, "Uploaded Successfully")
        return super(CreateSpecial, self).form_valid(form)
