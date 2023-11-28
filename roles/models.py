from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Role(models.Model):
    role = models.CharField(max_length=100, verbose_name="Role")
    team  = models.CharField(max_length=100, verbose_name="Team")

    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.role
