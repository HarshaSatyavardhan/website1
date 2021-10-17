from django.db import models

# Create your models here.

class researchpaper(models.Model):
    title = models.CharField(max_length=300, null=True)
    publication = models.CharField(max_length=200, null=True)
    link = models.URLField(max_length=500, null=True)
    authors = models.CharField(max_length=200, null=True)
    year = models.IntegerField(null=True)

    def __str__(self) :
        return self.title

class joinus(models.Model):
    data = models.TextField(max_length=1000, blank=True)

class alumini(models.Model):
    labalumini = models.CharField(max_length=300, null=True)
    currently = models.CharField(max_length=500, null=True)


