from django.db import models


class UserLanguage(models.Model):
    user_id = models.CharField(max_length=100, primary_key=True)
    lan = models.CharField(max_length=50)

    def __str__(self):
        return str(self.user_id)


class UserData(models.Model):
    user_id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Order(models.Model):
    user_id = models.CharField(max_length=100, primary_key=True)
    direction = models.CharField(max_length=100)
    day = models.CharField(max_length=100)
    hour = models.CharField(max_length=100)
    passengers = models.IntegerField()
    additional_service = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return str(self.user_id)
