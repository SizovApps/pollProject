from django.db import models


class Poll(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    slug = models.SlugField()
    numberOfVoters = models.PositiveIntegerField()
    timeOfBeg = models.DateTimeField()
    timeOfEnd = models.DateTimeField()
