from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from groups.forms import GroupCreateForm, GroupUpdateForm, GroupFilter
from groups.models import Group


class GroupListView(ListView):
    model = Group
    template_name = 'groups/list.html'

    def get_queryset(self):
        return GroupFilter(
            data=self.request.GET,
            queryset=Group.objects.all()
        )


class GroupCreateView(CreateView):
    model = Group
    form_class = GroupCreateForm
    success_url = reverse_lazy('groups:list')
    template_name = 'groups/create.html'


class GroupUpdateView(UpdateView):
    model = Group
    form_class = GroupUpdateForm
    success_url = reverse_lazy('groups:list')
    template_name = 'groups/update.html'


class GroupDeleteView(DeleteView):
    model = Group
    success_url = reverse_lazy('groups:list')
    template_name = 'groups/delete.html'
