from django.db import models
from django.core.validators import MaxValueValidator
import random
generate_key = random.randint(10000000, 99999999)

class Groups(models.Model):
    name = models.CharField(max_length=30, default="New Group here!")
    admin = models.TextField(default=None)
    description = models.TextField(default=f"{name} a brand new group! We try to supply the best of services.")
    key = models.IntegerField(validators=[MaxValueValidator(8)], default=generate_key)


class Teams(models.Model):
    name = models.CharField(max_length=30, default="New Team here!")
    admin = models.TextField(default=None)
    description = models.TextField(default=f"{name} a brand new team! We try to supply the best of services.")
    key = models.IntegerField(validators=[MaxValueValidator(8)], default=generate_key)


class Businesses(models.Model):
    name = models.CharField(max_length=30, default="New company here!")
    admin = models.TextField(default=None)
    description = models.TextField(default=f"{name} a brand new startup! We try to supply the best of services.")
    key = models.IntegerField(validators=[MaxValueValidator(8)], default=generate_key)

class GroupsManager(models.Model):
    members = models.TextField(default=[])
    max_members = models.IntegerField(default=10)
    ban_list = models.TextField(default=[])
    key = models.IntegerField(validators=[MaxValueValidator(8)], default=generate_key)

class TeamsManager(models.Model):
    members = models.TextField(default=[])
    max_members = models.IntegerField(default=50)
    ban_list = models.TextField(default=[])
    fundraiser = models.TextField(default=[])
    key = models.IntegerField(validators=[MaxValueValidator(8)], default=generate_key)

class BusinessesManager(models.Model):
    members = models.TextField(default=[])
    max_members = models.IntegerField(default=300)
    ban_list = models.TextField(default=[])
    current_project = models.TextField(default=None)
    meetings = models.TextField(default=None)
    key = models.IntegerField(validators=[MaxValueValidator(8)], default=generate_key)

class Messages(models.Model):
    account_key = models.IntegerField(validators=[MaxValueValidator(8)], default=None)
    group_key = models.IntegerField(validators=[MaxValueValidator(8)], default=None)
    username = models.TextField(default=None)
    message = models.TextField(default=None)
    sender = models.TextField(default=None)
    timestamp = models.DateTimeField(auto_now_add=True)

class Punishment(models.Model):
    punishment_type = models.TextField(default=None)
    account_key = models.TextField(default=None)
    reason = models.TextField(default="Not reason given.")
    timestamp = models.DateTimeField(auto_now_add=True)