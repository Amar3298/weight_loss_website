from django.db import models

class foodExercise(models.Model):
    Cname = models.CharField(max_length=50)
    Cemail = models.CharField(max_length=50)
    Cmessage = models.CharField(max_length=250)

    def __str__(self):
        return self.Cname
