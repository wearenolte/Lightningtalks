from django.contrib.auth.models import User
from django.db import models

TOPICS = (
    ('team_culture', 'Team Culture'),
    ('product_management', 'Product Mgmt'),
    ('marketing', 'Sales & Marketing'),
    ('tech', 'Technology'),
    ('design', 'Design'),
)

# Create your models here.
class Human(models.Model):
	user = models.ForeignKey(
        User, verbose_name="Human", related_name="user", blank=True, null=True
    )
	avatar = models.ImageField(upload_to='static/avatars/', null=True, blank=True)
	lightning = models.BooleanField('Available', default=True)
	current = models.BooleanField('Current', default=False)
	is_active = models.BooleanField('Active', default=True)

	class Meta:
		verbose_name = u'Human'
		verbose_name_plural = 'Humans'

	def __str__(self):
		return self.user.username

class Talks(models.Model):
	human = models.ForeignKey('Human')
	topic = models.CharField(
    max_length=100, choices=TOPICS, default='card'
  )
	name = models.CharField(max_length=200)
	link = models.URLField()
	cicle = models.IntegerField('Cicle')
	date = models.DateTimeField(auto_now_add=True)
	
	class Meta:
		verbose_name = u'Talk'
		verbose_name_plural = 'Talks'

	def __str__(self):
		return self.name