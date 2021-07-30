from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from courses.forms import CourseCreateForm, CourseUpdateForm, CourseFilter
from courses.models import Course


def get_course(request):

    courses = Course.objects.all()

    obj_filter = CourseFilter(data=request.GET, queryset=courses)

    return render(
        request=request,
        template_name='courses/list.html',
        context={'obj_filter': obj_filter}
    )


def create_course(request):

    if request.method == 'GET':

        form = CourseCreateForm()

    elif request.method == 'POST':

        form = CourseCreateForm(data=request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('courses:list'))

    return render(
        request=request,
        template_name='courses/create.html',
        context={'form': form}
    )


def update_courses(request, pk):

    courses = get_object_or_404(Course, id=pk)

    if request.method == 'GET':

        form = CourseUpdateForm(instance=courses)

    elif request.method == 'POST':

        form = CourseUpdateForm(
            instance=courses,
            data=request.POST
        )

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('courses:list'))

    return render(
        request=request,
        template_name='courses/update.html',
        context={'form': form}
    )


def delete_courses(request, pk):
    courses = get_object_or_404(Course, id=pk)
    if request.method == 'POST':
        courses.delete()
        return HttpResponseRedirect(reverse('courses:list'))

    return render(
        request=request,
        template_name='courses/delete.html',
        context={'course': courses}
    )
