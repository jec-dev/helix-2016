from django.db import models

class Query(models.Model):
	name = models.CharField(max_length=100, blank=False)
	email = models.EmailField(blank=False)
	message = models.CharField(max_length=255, blank=False)

	def __str__(self):
		return "By : %s" % self.name