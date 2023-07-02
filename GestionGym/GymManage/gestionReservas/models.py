from django.db import models

class Users(models.Model):
    name = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    password = models.CharField(max_length=30)
    isAdmin = models.BooleanField()

    def __str__(self):

        return self.name

class Penalties(models.Model):
    idUser = models.ForeignKey(Users, on_delete=models.CASCADE)
    date = models.DateField()
    reason = models.CharField(max_length=30)

    


class Hours(models.Model):
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return "" + self.date.strftime('%d-%m-%Y') + " " + self.time.strftime('%H:%M')

class Reserves(models.Model):
    idUser = models.ForeignKey(Users, on_delete=models.CASCADE)
    idHour = models.ForeignKey(Hours, on_delete=models.CASCADE)