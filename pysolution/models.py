from __future__ import unicode_literals
from django.db import models
from django.utils import timezone

# Create your models here.

class Pysolution(models.Model):
	developer    = models.ForeignKey('auth.User')
	question     = models.CharField(max_length=200)
	details      = models.TextField()
	solution     = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.question


