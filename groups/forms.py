import django_filters
from django.forms import ModelForm

from groups.models import Group


class GroupCreateForm(ModelForm):
    class Meta:
        model = Group
        fields = [
            'name',
            'start',
            'lesson_count',
            'lesson_passed',
        ]


class GroupUpdateForm(ModelForm):
    class Meta:
        model = Group
        fields = [
            'name',
            'start',
            'lesson_count',
            'lesson_passed',
        ]


class GroupFilter(django_filters.FilterSet):
    class Meta:
        model = Group
        fields = {
            'name': ['exact', 'icontains'],
            'lesson_count': ['lt', 'gt'],
        }
