from django.db import models

from faker import Faker


class Course(models.Model):
    name = models.CharField(max_length=120, null=False)
    create_datetime = models.DateTimeField(auto_now_add=True)
    update_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'

    @staticmethod
    def generate_course(count):
        faker = Faker()
        for _ in range(count):
            cr = Course(name=faker.job())
            cr.save()
