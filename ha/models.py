from django.db import models
from django.utils.timezone import now


# Create your models here.
class haItem (models.Model):
	subject = models.CharField (max_length=100)
	exercise = models.TextField ()
	info = models.TextField (blank=True)
	date_created_at = models.DateField (default=now)
	date_until = models.DateField ()
	author = models.CharField (max_length=100)

	def __str__(self):
		return self.exercise

	class Meta:
		verbose_name = "Hausaufgaben Eintrag"
		verbose_name_plural = "Hausaufgaben Einträge"

