from django.contrib import admin
from students.models import Students


class StudentAdmin(admin.ModelAdmin):
    list_display = [
        'first_name',
        'last_name',
        'birthdate',
        'groups_number',
    ]

    list_display_links = [
        'first_name',
        'last_name',
        'birthdate',
        'groups_number',
    ]

    list_per_page = 20

    fields = [
        ('first_name', 'last_name'),
        ('birthdate', 'age'),
        'email',
        ('groups_number', 'enroll_date', 'graduate_date')
    ]

    readonly_fields = ['age']
    search_fields = ['first_name', 'last_name']


admin.site.register(Students, StudentAdmin)
