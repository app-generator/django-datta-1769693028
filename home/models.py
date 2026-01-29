# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Dinghytype(models.Model):

    #__Dinghytype_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    py = models.IntegerField(null=True, blank=True)

    #__Dinghytype_FIELDS__END

    class Meta:
        verbose_name        = _("Dinghytype")
        verbose_name_plural = _("Dinghytype")


class Registereddinghy(models.Model):

    #__Registereddinghy_FIELDS__
    sail = models.CharField(max_length=255, null=True, blank=True)
    dinghy_type = models.ForeignKey(DinghyType, on_delete=models.CASCADE)

    #__Registereddinghy_FIELDS__END

    class Meta:
        verbose_name        = _("Registereddinghy")
        verbose_name_plural = _("Registereddinghy")


class League(models.Model):

    #__League_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)

    #__League_FIELDS__END

    class Meta:
        verbose_name        = _("League")
        verbose_name_plural = _("League")


class Race(models.Model):

    #__Race_FIELDS__
    date_time = models.DateTimeField(blank=True, null=True, default=timezone.now)
    league = models.ForeignKey(League, on_delete=models.CASCADE)

    #__Race_FIELDS__END

    class Meta:
        verbose_name        = _("Race")
        verbose_name_plural = _("Race")


class Participant(models.Model):

    #__Participant_FIELDS__
    member = models.CharField(max_length=255, null=True, blank=True)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)

    #__Participant_FIELDS__END

    class Meta:
        verbose_name        = _("Participant")
        verbose_name_plural = _("Participant")



#__MODELS__END
