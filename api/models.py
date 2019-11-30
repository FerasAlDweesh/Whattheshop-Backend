from django.db import models
from django.contrib.auth.models import User

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


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	orders = models.ManyToManyField(Order, on_delete=models.CASCADE)

	def __str__(self):
		return str(self.user)