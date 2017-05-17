from __future__ import unicode_literals
from django.db import models

class mcafee_updatedstate(models.Model):
    fechaingreso = models.DateField(primary_key=True)
    total = models.IntegerField()
    updated = models.IntegerField()
    noupdated = models.IntegerField()
    totalproceso = models.IntegerField()
    db = models.IntegerField()
    class Meta:
         db_table = "mcafee_updatedstate"       