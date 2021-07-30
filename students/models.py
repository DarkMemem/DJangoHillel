import datetime

from django.db import models

from groups.models import Group
from core.models import Person


class Students(Person):
    groups_number = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, related_name='students', blank=True)
    enroll_date = models.DateField(default=datetime.date.today, null=True)
    graduate_date = models.DateField(default=datetime.date.today, null=True)

    create_datetime = models.DateTimeField(auto_now_add=True)
    update_datetime = models.DateTimeField(auto_now=True)

    @classmethod
    def _generate(cls):
        super()._generate()
