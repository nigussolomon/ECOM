from django.db import models
from django.contrib.auth.models import User

NOTIFICATION_STATUSES = (
    ('unread', 'UNREAD'),
    ('read', 'READ'),
)

NOTIFICATION_TYPES = (
    ('urgent', 'URGENT'),
    ('notice', 'NOTICE'),
    ('warning', 'WARNING'),
)

class EcomProfile(models.Model):
    user = models.OneToOneField(User, blank=False, null=False, on_delete=models.CASCADE)
    first_name = models.CharField(blank=False, null=False, max_length=50)
    middle_name = models.CharField(blank=False, null=False, max_length=50)
    last_name = models.CharField(blank=False, null=False, max_length=50)
    phone_number = models.CharField(blank=False, null=False, max_length=20)
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=80)
    building_number = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.first_name + " " + self.middle_name + " " + self.last_name

class Notification(models.Model):
    user = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE)
    title = models.CharField(blank=False, null=False, max_length=150)
    message = models.TextField(blank=False, null=False) 
    delivery_date = models.DateField(blank=False, null=False)
    notification_status = models.CharField(blank=False, null=False, choices=NOTIFICATION_STATUSES, default='unread', max_length=20)
    notification_type = models.CharField(blank=False, null=False, choices=NOTIFICATION_TYPES, default='notice', max_length=20)

    def __str__(self) -> str:
        return self.title