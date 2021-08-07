from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from teachers.forms import TeachersCreateForm, TeachersUpdateForm, TeachersFilter
from teachers.models import Teachers


class TeacherListView(ListView):
    paginate_by = 20
    model = Teachers
    template_name = 'teachers/list.html'

    def get_filter(self):
        return TeachersFilter(
            data=self.request.GET,
            queryset=self.model.objects.all()
        )

    def get_queryset(self):
        return self.get_filter().qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_filter'] = self.get_filter()

        return context


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
