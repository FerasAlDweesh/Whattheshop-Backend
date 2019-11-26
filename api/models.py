from django.db import models

class Dinosaur(models.Model):
	name = models.CharField(max_length=105)

	def __str__(self):
		return self.name