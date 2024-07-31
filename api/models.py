from django.db import models


class UserData(models.Model):
    user_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name
