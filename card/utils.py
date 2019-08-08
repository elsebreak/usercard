from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from .models import *

class ObjectReadMixin:
    model = None
    template = None

    def get(self, request, uniq):
        obj = get_object_or_404(self.model, uniq__iexact=uniq)
        return render(request, self.template, context={self.model.__name__.lower(): obj, 'admin_object': obj})

class ObjectCreateMixin:
    model_form = None
    template = None

    def get(self, request):
        form = self.model_form()
        return render(request, self.template, context={'form': form})

    def post(self, request):
        bound_form = self.model_form(request.POST)

        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(new_obj)
        return render(request, self.template, context={'form': bound_form})

class ObjectUpdateMixin:
    model = None
    model_form = None
    template = None

    def get(self, request, uniq):
        obj = self.model.objects.get(uniq__iexact=uniq)
        bound_form = self.model_form(instance=obj)
        return render(request, self.template, context={'form': bound_form, self.model.__name__.lower(): obj})

    def post(self, request, uniq):
        obj = self.model.objects.get(uniq__iexact=uniq)
        bound_form = self.model_form(request.POST, instance=obj)

        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(new_obj)
        return render(request, self.template, context={'form': bound_form, self.model.__name__.lower(): obj})

class ObjectDeleteMixin:
    model = None
    template = None
    redirect_url = None

    def get(self, request, uniq):
        obj = self.model.objects.get(uniq__iexact=uniq)
        return render(request, self.template, context={self.model.__name__.lower(): obj})

    def post(self, request, uniq):
        obj = self.model.objects.get(uniq__iexact=uniq)
        obj.delete()
        return redirect(reverse(self.redirect_url))
