from django.contrib import admin
from students.models import Students

from groups.models import Group


class StudentInline(admin.TabularInline):
    model = Students
    fields = [
        'last_name',
        'first_name',
        'email',
        'birthdate',
        'age',
    ]

    readonly_fields = ['age']

    show_change_link = True
    extra = 0


class GroupAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'start',
    ]
    fields = [
        'name',
        'courses',
        'teachers',
        'lesson_count',
        'lesson_passed',
    ]
    inlines = [StudentInline]
    search_fields = [
        'name',
        'start',
        'courses',
    ]

    list_per_page = 20


admin.site.register(Group, GroupAdmin)
