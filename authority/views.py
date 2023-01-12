from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views import View
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .models import User
from .forms import UserCreateForm
from .forms import UserUpdateForm


class UserCreateView(SuccessMessageMixin, CreateView):
    form_class = UserCreateForm
    template_name = 'registration/register.html'
    success_message = 'Account Created Successfully'
    success_url = reverse_lazy("auth:login")


class UserUpdateView(LoginRequiredMixin, View):
  template_name = 'registration/update-profile.html'
  model = User
  success_url = 'auth:update'

  def get(self, request):
    user = get_object_or_404(self.model, id=request.user.id)
    form = UserUpdateForm(instance=user)
    context = {'form': form}
    return render(request, self.template_name, context)

  def post(self, request):
    user = get_object_or_404(self.model, id=request.user.id)
    form = UserUpdateForm(request.POST, request.FILES, instance=user)
    if not form.is_valid():
      context = {'form': form}
      return render(request, self.template_name, context)
    form.save()
    messages.success(request, "Profile Updated Successfully")
    return redirect(self.success_url)

