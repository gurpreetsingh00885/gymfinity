from django.db import models
from django.contrib.gis.db.models import PointField


class Gym(models.Model):

	location = PointField(blank=False)
	name = models.CharField(max_length = 100, blank=False)

	def __str__(self):
		return self.name