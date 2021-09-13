from django.db import models
from django.contrib.auth.models import  User
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import json

# Create your models here.


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    notification = models.TextField()
    is_seen = models.BooleanField(default=False)


    def save(self, *args, **kwargs):

        channel_layer = get_channel_layer()

        notifications =  Notification.objects.all().count()

        data ={"count":notifications, 'current_notif':self.notification}

        async_to_sync(channel_layer.group_send)(
            # self.room_group_name,
            # self.channel_name

            "test_consumer_group", {
                "type":"send_notification",
                "value":json.dumps(data)
            }
        )

        print("------------yes its working model -------------")
        super(Notification, self).save(*args, **kwargs)