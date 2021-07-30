import django_filters
from django.forms import ModelForm

from courses.models import Course


class CourseBaseForm(ModelForm):
    class Meta:
        model = Course
        fields = "__all__"
        exclude = [
            'create_datetime',
            'update_datetime',
        ]


class CourseCreateForm(CourseBaseForm):
    pass


class CourseUpdateForm(CourseBaseForm):
    pass


class CourseFilter(django_filters.FilterSet):
    class Meta:
        model = Course
        fields = {
            'name': ['icontains']
        }
