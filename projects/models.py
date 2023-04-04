from django.db import models
import uuid

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    source_link = models.CharField(max_length=2000, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)   # create a time stamp when the instance is created
    # actually, django creates an id by default, but you shold use uuid in some cases
    id = models.UUIDField(
        default=uuid.uuid4, # encoding type
        unique=True,    # no other same number
        primary_key=True,   # tell djnago to use id as a primary key
        editable=False  # protect editing id from users
    )

    def __str__(self):
        return self.title   #  to show the title in the admin panel