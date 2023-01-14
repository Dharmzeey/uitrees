from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect

class AdminRequiredMixin(LoginRequiredMixin):
  def dispatch(self, request, *args, **kwargs):
    if not request.user.is_superuser:
      return redirect('home')
    return super().dispatch(request, *args, **kwargs)