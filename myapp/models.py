from django.db import models

class Todo(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    class Meta:
        app_label = 'myapp'

    def __str__(self):
        return self.name

