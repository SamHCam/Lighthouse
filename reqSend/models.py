import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Request(models.Model):
    request_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('request published')

    def __str__(self):
        return self.request_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
   
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class Expense(models.Model):
    request = models.ForeignKey(Request, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    amount = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text