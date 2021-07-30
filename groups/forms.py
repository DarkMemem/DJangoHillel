import django_filters
from django.forms import ModelForm

from groups.models import Group


class GroupBaseForm(ModelForm):
    class Meta:
        model = Group
        fields = '__all__'


class GroupCreateForm(GroupBaseForm):
    pass


class GroupUpdateForm(GroupBaseForm):
    pass


class GroupFilter(django_filters.FilterSet):
    class Meta:
        model = Group
        fields = {
            'name': ['exact', 'icontains'],
            'lesson_count': ['lt', 'gt'],
        }
