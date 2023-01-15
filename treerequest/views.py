from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView
from django.views import View
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib import messages

from utilities.mixins import AdminRequiredMixin
from utilities.location_validator import validate_location

from .models import RequestTree


class RequestTreeView(LoginRequiredMixin, CreateView):
    model = RequestTree
    fields = ['location_name', 'location_description', 'tree_picture', 'tree_picture2', 'coordinates', 'latitude', 'longitude']
    template_name = 'treerequest/request-tree.html'
    success_url = reverse_lazy('home:home')
    login_url = reverse_lazy('user:register')
    
    def form_valid(self, form):
        form.instance.requester = self.request.user
        lat = form.instance.latitude
        long = form.instance.longitude
        check = validate_location(long, lat)
        if check == False:
            messages.error(self.request, "Sorry, request declined as You are outside University of Ibadan")
            return render(self.request, self.template_name, {'form': form})
        else:
            form.save()
            messages.success(self.request, "Tree request submitted Successfully")
            return super(RequestTreeView, self).form_valid(form)


class ViewRequest(AdminRequiredMixin, View):
    template_name = "treerequest/tree-requests.html"
    def get(self, request):
        tree_requests = RequestTree.objects.filter(validated=False)
        context = {"tree_requests": tree_requests}
        return render(request, self.template_name, context)


class RequestDetails(AdminRequiredMixin, DetailView):
    model = RequestTree
    template_name = "treerequest/request-detail.html"
    context_object_name = "tree"
    
