from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy

from .models import Profile
from .forms import ProfileCreateFrom
from .forms import ProfileUpdateForm


class ProfileCreateView(CreateView):
    form_class = ProfileCreateFrom
    template_name = 'registration/register.html'
    success_url = reverse_lazy("auth:login")


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
  model = Profile
  form_class = ProfileUpdateForm
  template_name = 'registration/register.html'

  def get_queryset(self):
    qs = super(ProfileUpdateView, self).get_queryset()
    return qs.filter(user=self.request.user)

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super(ProfileUpdateView, self).form_valid(form)
  success_url = reverse_lazy("home:home")
