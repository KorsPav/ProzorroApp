from django.db import models
from django.contrib.auth import get_user_model


class Tender(models.Model):
    hash = models.TextField()
    created_date = models.DateTimeField(auto_now=True)
    updated_date = models.DateTimeField(auto_now_add=True)
    data = models.JSONField()
    tender_start_date = models.DateTimeField(null=True)
    tender_end_date = models.DateTimeField(null=True)
    last_status = models.TextField(null=True)


class UserStat(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    tenders = models.ManyToManyField(Tender)
