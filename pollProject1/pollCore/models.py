from django.db import models
from django.shortcuts import reverse


class Poll(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    slug = models.SlugField()
    numberOfVoters = models.PositiveIntegerField()
    timeOfBeg = models.DateTimeField()
    timeOfEnd = models.DateTimeField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('poll_detail_url', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['-timeOfBeg']
