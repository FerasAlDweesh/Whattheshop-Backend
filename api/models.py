from django.db import models

class Dinosaur(models.Model):
	CHOICES = (('common', 'common'),
		('uncommon', 'uncommon'), ('rare', 'rare'),
		('exotic', 'exotic'), ('legendary', 'legendary')

		)
	name = models.CharField(max_length=105)
	price = models.PositiveIntegerField()
	rarity = models.CharField(max_length=105, choices=CHOICES)
	description = models.TextField()
	image = models.ImageField(null=True, blank=True)

	def __str__(self):
		return self.name