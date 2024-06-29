from django.db import models
from django.utils import timezone

class TodoList(models.Model):
    """
    Model representing a to-do list item.
    """
    title = models.CharField(max_length=100)
    details = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        """
        String representation of the TodoList model.
        """
        return self.title

    class Meta:
        """
        Meta class for TodoList model to define additional settings.
        """
        verbose_name = "To-Do List"
        verbose_name_plural = "To-Do Lists"
        ordering = ['-date']
