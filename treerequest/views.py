# from django.views import View
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import RequestTree


class RequestTreeView(CreateView):

    model = RequestTree
    fields = '__all__'
    template_name = 'treerequest/tree_request.html'
    success_url = reverse_lazy('home:home')
