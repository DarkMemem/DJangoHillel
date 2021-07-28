from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from groups.forms import GroupCreateForm, GroupUpdateForm, GroupFilter
from groups.models import Group


def get_group(request):

    groups = Group.objects.all()

    obj_filter = GroupFilter(data=request.GET, queryset=groups)

    return render(
        request=request,
        template_name='groups/list.html',
        context={'obj_filter': obj_filter}
    )


def create_group(request):

    if request.method == 'GET':

        form = GroupCreateForm()

    elif request.method == 'POST':

        form = GroupCreateForm(data=request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('groups:list'))

    return render(
        request=request,
        template_name='groups/create.html',
        context={'form': form},
    )


def update_group(request, pk):

    groups = get_object_or_404(Group, id=pk)

    if request.method == 'GET':

        form = GroupUpdateForm(instance=groups)

    elif request.method == 'POST':

        form = GroupUpdateForm(
            instance=groups,
            data=request.POST
        )

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('groups:list'))

    return render(
        request=request,
        template_name='groups/update.html',
        context={'form': form}
    )


def delete_group(request, pk):

    groups = get_object_or_404(Group, id=pk)

    if request.method == 'POST':
        groups.delete()
        return HttpResponseRedirect(reverse('groups:list'))

    return render(
        request=request,
        template_name='groups/delete.html',
        context={'group': groups}
    )
