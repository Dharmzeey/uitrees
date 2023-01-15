from django.shortcuts import render
from django.views.generic import CreateView
from django.views import View
from django.urls import reverse_lazy
from django.contrib import messages
from django.conf import settings

# User = settings.AUTH_USER_MODEL
from user.models import User
from treerequest.models import RequestTree

from utilities.mixins import AdminRequiredMixin
from utilities.location_validator import validate_location

from .models import Upload
from .forms import UploadTreeForm

# Create your views here.


class CreateTree(AdminRequiredMixin, CreateView):
    # model = Upload
    form_class = UploadTreeForm
    success_url = reverse_lazy('upload:upload')
    template_name = 'upload/upload_form.html'

    def form_valid(self, form):
        form.instance.uploaded_by = self.request.user
        lat = form.instance.latitude
        long = form.instance.longitude
        check = validate_location(long, lat)
        if check == False:
            messages.error(self.request, "Sorry, You can not upload outside University of Ibadan")
            return render(self.request, self.template_name, {'form': form})
        else:
            form.save()
            messages.success(self.request, "Tree Uploaded Successfully")
            return super(CreateTree, self).form_valid(form)
    
class UploadTreeRequest(AdminRequiredMixin, CreateView):
    form_class = UploadTreeForm
    success_url = reverse_lazy('upload:upload')
    template_name = 'upload/upload_form.html'

    def form_valid(self, form):
        form.instance.uploaded_by = self.request.user
        request_id = RequestTree.objects.get(id=self.kwargs['pk'])
        form.instance.requested_by = request_id.requester
        
        lat = form.instance.latitude
        long = form.instance.longitude
        check = validate_location(long, lat)
        if check == False:
            messages.success(self.request, "Sorry, You can not upload outside University of Ibadan")
            return render(self.request, self.template_name, {'form': form})
        else:        
            form.save()
            request_id.validated = True
            request_id.save()
            messages.success(self.request, "Tree Request Uploaded Successfully")
            return super(UploadTreeRequest, self).form_valid(form)


# class CreateFormTree(View):
#     template_name = 'upload/upload_form.html'
#     success_url = reverse_lazy('upload:success')
#
#     def get(self, request):
#         form = CreateModelForm()
#         context = {'form': form}
#         return render(request, self.template_name, context)
#
#     def post(self, request):
#         form = CreateModelForm(request.POST)
#         if not form.is_valid():
#             print('not valid')
#             print(request.POST)
#             context = {'form': form}
#             return render(request, self.template_name, context)
#         else:
#             form.save()
#             CreateModelForm()
#             print('valid')
#             return redirect(self.success_url)


class Success(View):
    template_name = 'upload/success_page.html'

    def get(self, request):

        return render(request, self.template_name)
