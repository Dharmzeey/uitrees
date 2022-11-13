from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib import messages

from .models import RequestTree


class RequestTreeView(CreateView):
    model = RequestTree
    fields = '__all__'
    template_name = 'treerequest/tree_request.html'
    success_url = reverse_lazy('home:home')
    
    def form_valid(self, form):
        messages.success(self.request, "Tree request submitted Successfully")
        return super(RequestTreeView, self).form_valid(form)
