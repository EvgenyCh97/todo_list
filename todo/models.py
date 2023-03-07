from django.db import models
from django.utils import timezone


class Todo(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    # deadline_date =

    def create(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
