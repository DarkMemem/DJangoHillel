
from django.db import models

from core.models import Person


class Teachers(Person):
    create_datetime = models.DateTimeField(auto_now_add=True)
    update_datetime = models.DateTimeField(auto_now=True)

    @classmethod
    def _generate(cls):
        super()._generate()

