from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django_countries.fields import CountryField
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType

GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Others', 'Others'),
)

class Student(models.Model):
    user = models.ForeignKey(User)
    avatar = models.ImageField(upload_to="profile/editors/", null=True, blank=True)
    address = models.CharField(max_length=60, blank=True, null=True)
    nationality = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=60, null=True, blank=True, choices=GENDER_CHOICES)
    country = CountryField(blank_label="(select country)", null=True, blank=True)

    def __str__(self):
        return u'%s %s' %(self.user.first_name, self.user.last_name)
