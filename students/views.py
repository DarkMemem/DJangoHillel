from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from students.forms import StudentsUpdateForm, StudentsCreateForm, StudentsFilter
from students.models import Students


class StudentListView(ListView):
    model = Students
    template_name = 'students/list.html'

    def get_queryset(self):
        return StudentsFilter(
            data=self.request.GET,
            queryset=self.model.objects.all()
        )


class StudentCreateView(CreateView):
    model = Students
    form_class = StudentsCreateForm
    success_url = reverse_lazy('students:list')
    template_name = 'students/create.html'


class StudentUpdateView(UpdateView):
    model = Students
    form_class = StudentsUpdateForm
    success_url = reverse_lazy('students:list')
    template_name = 'students/update.html'


class StudentDeleteView(DeleteView):
    model = Students
    success_url = reverse_lazy('students:list')
    template_name = 'students/delete.html'
