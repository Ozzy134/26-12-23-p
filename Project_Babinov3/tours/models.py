from django.db import models

class Countries(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Tours(models.Model):
    title = models.CharField(max_length=20)
    countries = models.ForeignKey(Countries, on_delete=models.CASCADE)
    hotel = models.CharField(max_length=15)
    chel = models.IntegerField()
    price = models.IntegerField()
    list = models.TextField()

    def __str__(self):
        return self.title
