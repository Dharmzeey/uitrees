from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views import View
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .models import Profile
from .forms import ProfileCreateForm
from .forms import ProfileUpdateForm


class ProfileCreateView(CreateView):
    form_class = ProfileCreateForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy("auth:login")


class ProfileUpdateView(LoginRequiredMixin, View):
  template_name = 'registration/register.html'
  model = Profile
  success_url = 'auth:update'

  def get(self, request):
    owner = get_object_or_404(self.model, owner=request.user)
    form = ProfileUpdateForm(instance=owner)
    context = {'form': form}
    return render(request, self.template_name, context)

  def post(self, request):
    owner = get_object_or_404(self.model, owner=request.user)
    form = ProfileUpdateForm(request.POST, request.FILES, instance=owner)
    if not form.is_valid():
      context = {'form': form}
      return render(request, self.template_name, context)
    form.save()
    messages.success(request, "Profile Updated Successfully")
    return redirect(self.success_url)

