from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from .models import MyUserCreationModel
from .forms import MyUserUpdateForm

from .forms import MyUserCreationFrom


class MyUserCreationView(CreateView):
    form_class = MyUserCreationFrom
    template_name = 'registration/register.html'
    success_url = reverse_lazy("auth:login")


class MyUserUpdateView(LoginRequiredMixin, UpdateView):
  model = MyUserCreationModel
  form_class = MyUserUpdateForm
  template_name = 'registration/register.html'

  def get_queryset(self):
    qs = super(MyUserUpdateView, self).get_queryset()
    return qs.filter(username=self.request.user)
  success_url = reverse_lazy("home:home")
