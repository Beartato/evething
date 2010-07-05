from django.db import models


class Region(models.Model):
	id = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=30)
	
	def __unicode__(self):
		return self.name

class Item(models.Model):
	id = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=50)
	
	def __unicode__(self):
		return self.name

class ItemPrice(models.Model):
	item = models.ForeignKey(Item)
	region = models.ForeignKey(Region)
	sell_price = models.DecimalField(max_digits=15, decimal_places=2)
	sell_volume = models.IntegerField()
	buy_price = models.DecimalField(max_digits=15, decimal_places=2)
	buy_volume = models.IntegerField()

class Blueprint(models.Model):
	id = models.IntegerField(primary_key=True)
	#item_id = models.ForeignKey(Item)
	components = models.ManyToManyField(Item, through='BlueprintComponent')
	
	production_time = models.IntegerField()
	waste_factor = models.IntegerField()
	
	def __unicode__(self):
		return self.name

class BlueprintComponent(models.Model):
	item = models.ForeignKey(Item)
	blueprint = models.ForeignKey(Blueprint)
	count = models.IntegerField()

class BlueprintCopy(models.Model):
	blueprint = models.ForeignKey(Blueprint)
	material_level = models.IntegerField()
	productivity_level = models.IntegerField()

class Character(models.Model):
	name = models.CharField(max_length=30)
	api_key = models.CharField(max_length=64)
	industry_skill = models.IntegerField()
	production_efficiency_skill = models.IntegerField()
	factory_cost = models.DecimalField(max_digits=8, decimal_places=2)
	factory_per_hour = models.DecimalField(max_digits=8, decimal_places=2)
	sales_tax = models.DecimalField(max_digits=4, decimal_places=2)
	brokers_fee = models.DecimalField(max_digits=4, decimal_places=2)
	
	def __unicode__(self):
		return self.name
