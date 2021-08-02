from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from groups.forms import GroupCreateForm, GroupUpdateForm, GroupFilter
from groups.models import Group


class GroupListView(ListView):
    paginate_by = 20
    model = Group
    template_name = 'groups/list.html'

    def get_filter(self):
        return GroupFilter(
            data=self.request.GET,
            queryset=self.model.objects.all().select_related('courses')
        )

    def get_queryset(self):
        return self.get_filter().qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_filter'] = self.get_filter()

        return context


class GroupCreateView(LoginRequiredMixin, CreateView):
    model = Group
    form_class = GroupCreateForm
    success_url = reverse_lazy('groups:list')
    template_name = 'groups/create.html'

    def form_valid(self, form):
        result = super().form_valid(form)
        messages.success(self.request, f'Group {form.cleaned_data["name"]} was successfully created.')

        return result


class GroupUpdateView(LoginRequiredMixin, UpdateView):
    model = Group
    form_class = GroupUpdateForm
    success_url = reverse_lazy('groups:list')
    template_name = 'groups/update.html'

    def form_valid(self, form):
        result = super().form_valid(form)
        messages.success(self.request, f'Group {form.cleaned_data["name"]} was successfully updated.')

        return result


class GroupDeleteView(LoginRequiredMixin, DeleteView):
    model = Group
    success_url = reverse_lazy('groups:list')
    template_name = 'groups/delete.html'

    def delete(self, *args, **kwargs):
        result = super(GroupDeleteView, self).delete(*args, **kwargs)
        messages.success(self.request, 'Group was successfully deleted')

        return result
