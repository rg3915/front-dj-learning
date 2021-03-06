import json
from django.core import serializers
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy as r
from django.views.generic import ListView, DetailView
from django.views.generic import UpdateView, DeleteView
from .mixins import NameSearchMixin
from .models import Person, Phone
from .forms import PersonForm


def home(request):
    return render(request, 'index.html')


class PersonList(NameSearchMixin, ListView):
    model = Person
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(PersonList, self).get_context_data(**kwargs)
        context['form'] = PersonForm()
        return context


person_detail = DetailView.as_view(model=Person)


def person_create(request):
    if request.method == 'POST':
        if request.is_ajax():
            form = PersonForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponse('OK')
            else:
                return HttpResponse(status=400)
        else:
            return render(request, 'core/person_form.html', {'form': PersonForm(request.POST)})
    return render(request, 'core/person_form.html', {'form': PersonForm()})


person_update = UpdateView.as_view(model=Person, form_class=PersonForm)

person_delete = DeleteView.as_view(
    model=Person,
    success_url=r('core:person_list')
)


def person_phones(request, pk):
    phones = Phone.objects.filter(person=pk)
    data = serializers.serialize('json', phones)
    return HttpResponse(data, content_type='application/json')


def person_phone_create(request):
    if request.method == 'POST':
        person_pk = request.POST['person']
        person = Person.objects.get(pk=person_pk)
        phone = request.POST['phone']
        Phone.objects.create(person=person, phone=phone)
        data = phone
    return HttpResponse(data, content_type='application/json')
