from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin

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


class TeacherCreateView(LoginRequiredMixin, CreateView):
    model = Teachers
    form_class = TeachersCreateForm
    success_url = reverse_lazy('teachers:list')
    template_name = 'teachers/create.html'


class TeacherUpdateView(LoginRequiredMixin, UpdateView):
    model = Teachers
    form_class = TeachersUpdateForm
    success_url = reverse_lazy('teachers:list')
    template_name = 'teachers/update.html'


class TeacherDeleteView(LoginRequiredMixin, DeleteView):
    model = Teachers
    success_url = reverse_lazy('teachers:list')
    template_name = 'teachers/delete.html'
