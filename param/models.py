from django.db import models

# Create your models here.



class Centre(models.Model):
    code = models.IntegerField()
    nom = models.CharField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    description = models.TextField()

    def __str__(self):
        return self.nom
