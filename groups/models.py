import datetime
import random

from django.db import models
from faker import Faker

from teachers.models import Teachers
from courses.models import Course


class Group(models.Model):
    name = models.CharField(max_length=40)
    start = models.DateField(default=datetime.date.today)
    lesson_count = models.IntegerField(default=16, null=False)
    lesson_passed = models.IntegerField(default=0, null=False)

    teachers = models.ManyToManyField(to=Teachers, related_name='groups')

    create_datetime = models.DateTimeField(auto_now_add=True)
    update_datetime = models.DateTimeField(auto_now=True)
    courses = models.OneToOneField(Course, null=True, blank=True, on_delete=models.SET_NULL, related_name='groups')

    def __str__(self):
        return self.name

    @staticmethod
    def generate_groups(count):
        faker = Faker("ru_Ru")
        for _ in range(count):
            gr = Group(
                name=faker.job(),
                start=faker.date_time_this_decade(),
                lesson_count=random.randint(1, 16),
                lesson_passed=random.randint(1, 16)
            )
            gr.save()
