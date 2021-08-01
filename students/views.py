from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

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


class StudentCreateView(LoginRequiredMixin, CreateView):
    model = Students
    form_class = StudentsCreateForm
    success_url = reverse_lazy('students:list')
    template_name = 'students/create.html'

    def form_valid(self, form):
        result = super().form_valid(form)
        messages.success(self.request, f"Students {form.cleaned_data['first_name']} was successfully created.")

        return result


class StudentUpdateView(LoginRequiredMixin, UpdateView):
    model = Students
    form_class = StudentsUpdateForm
    success_url = reverse_lazy('students:list')
    template_name = 'students/update.html'

    def form_valid(self, form):
        result = super().form_valid(form)
        messages.success(self.request, f"Student {form.cleaned_data['first_name']} was successfully update.")

        return result


class StudentDeleteView(LoginRequiredMixin, DeleteView):
    model = Students
    success_url = reverse_lazy('students:list')
    template_name = 'students/delete.html'

    def delete(self, *args, **kwargs):
        result = super(DeleteView, self).delete(*args, **kwargs)
        messages.success(self.request, f"Student  was successfully deleted.")

        return result
