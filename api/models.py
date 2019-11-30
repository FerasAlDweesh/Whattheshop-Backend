from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Dinosaur(models.Model):
	CHOICES = (('common', 'common'),
		('uncommon', 'uncommon'), ('rare', 'rare'),
		('exotic', 'exotic'), ('legendary', 'legendary')

		)
	name = models.CharField(max_length=105)
	price = models.DecimalField(default=0.00, decimal_places=2, max_digits=100)
	inventory = models.PositiveIntegerField()
	rarity = models.CharField(max_length=105, choices=CHOICES)
	description = models.TextField()
	image = models.ImageField(null=True, blank=True)

	def __str__(self):
		return self.name

class Order(models.Model):
	# id
	customer = models.ForeignKey(User, on_delete = models.CASCADE)
	date = models.DateTimeField(auto_now_add=True)
	item = models.ManyToManyField(Dinosaur, through = 'OrderedItem') #Item and Quantity purchased (OrderedItem)

	def __str__(self):
		return self.customer

class OrderedItem(models.Model):
	item = models.ForeignKey(Dinosaur, on_delete = models.CASCADE) #Name and Price of Item(Dinosaur)
    quantity = models.IntegerField(default=0,validators=[MinValueValidator(1)])
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
	# calculated in front end:

	#  - total quantity
	#  - total price