from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

from teachers.forms import TeachersCreateForm, TeachersUpdateForm, TeachersFilter
from teachers.models import Teachers


class TeacherListView(ListView):
    model = Teachers
    template_name = 'teachers/list.html'

    def get_queryset(self):
        return TeachersFilter(
            data=self.request.GET,
            queryset=self.model.objects.all()
        )


class TeacherCreateView(CreateView):
    model = Teachers
    form_class = TeachersCreateForm
    success_url = reverse_lazy('teachers:list')
    template_name = 'teachers/create.html'


class TeacherUpdateView(UpdateView):
    model = Teachers
    form_class = TeachersUpdateForm
    success_url = reverse_lazy('teachers:list')
    template_name = 'teachers/update.html'


class TeacherDeleteView(DeleteView):
    model = Teachers
    success_url = reverse_lazy('teachers:list')
    template_name = 'teachers/delete.html'
