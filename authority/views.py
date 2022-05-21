from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy

from .models import Profile
from .forms import ProfileCreateFrom
from .forms import ProfileUpdateForm


class ProfileCreateView(CreateView):
    form_class = ProfileCreateFrom
    template_name = 'registration/register.html'
    success_url = reverse_lazy("auth:login")


class ProfileUpdateView(LoginRequiredMixin, View):
  template_name = 'registration/register.html'
  model = Profile
  success_url = 'auth:update'

  def get(self, request):
    owner = get_object_or_404(self.model, user=request.user)
    form = ProfileUpdateForm(instance=owner)
    context = {'form': form}
    return render(request, self.template_name, context)

  def post(self, request):
    owner = get_object_or_404(self.model, user=request.user)
    form = ProfileUpdateForm(request.POST, request.FILES, instance=owner)
    if not form.is_valid():
      context = {'form': form}
      return render(request, self.template_name, context)
    form.save()
    return redirect(self.success_url)

# THIS WAS MY FIRST METHOD OF UPDATE VIEWS, BUT I WANT THE PK TO BE CONCEALED
# class ProfileUpdateView(LoginRequiredMixin, UpdateView):
#   slug_field = "user"
#   slug_url_kwarg = "user"
#   model = Profile
#   form_class = ProfileUpdateForm
#   template_name = 'registration/register.html'
#
#   def get_queryset(self):
#     qs = super(ProfileUpdateView, self).get_queryset()
#     return qs.filter(user=self.request.user)
#
#   def form_valid(self, form):
#     form.instance.user = self.request.user
#     return super(ProfileUpdateView, self).form_valid(form)
#   success_url = reverse_lazy("home:home")
