from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.views import View
from .models import Upload

from django.http  import HttpResponse
from .forms import CreateModelForm
from django.urls import reverse_lazy

# Create your views here.


class ListTree(View):
    template_name = 'upload/upload_page.html'

    def get(self, request):
        all_trees = Upload.objects.all()
        context = {'all_trees': all_trees}

        return render(request, self.template_name, context)


class CreateTree(CreateView):
    model = Upload
    fields = '__all__'
    success_url = reverse_lazy('upload:upload')


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

