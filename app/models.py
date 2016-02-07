from django.db import models
from datetime import datetime

class Query(models.Model):
	name = models.CharField(max_length=100, blank=False)
	email = models.EmailField(blank=False)
	message = models.CharField(max_length=255, blank=False)
	pub_date = models.DateTimeField(default = datetime.now, blank = True)

	def __str__(self):
		return "By : %s" % self.name