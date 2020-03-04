from datetime import datetime, timedelta

from django.db import models

from users import utils
from . import constants

# Create your models here.
from commons.abstracts import TimeStamp


class User(TimeStamp):

    first_name = models.CharField(
        max_length=constants.CHARACTER_LIMIT_MEDIUM
    )

    last_name = models.CharField(
        max_length=constants.CHARACTER_LIMIT_MEDIUM
    )

    company_name = models.CharField(
        max_length=constants.CHARACTER_LIMIT_MEDIUM
    )

    dob = models.DateField()

    city = models.CharField(max_length=constants.CHARACTER_LIMIT_LOW)

    state = models.CharField(max_length=constants.CHARACTER_LIMIT_LOW)

    zip = models.CharField(max_length=constants.CHARACTER_LIMIT_LOW)

    email = models.CharField(max_length=constants.CHARACTER_LIMIT_MEDIUM)

    web = models.CharField(max_length=constants.CHARACTER_LIMIT_HIGH)

    objects = models.Manager()

    @property
    def age(self):
        return utils.dob_to_age(self.dob)

    @age.setter
    def age(self, ag):
        self.dob = utils.age_to_dob(ag)
