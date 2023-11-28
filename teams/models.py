from django.db import models
from django.contrib.auth.models import User

class Team(models.Model):
    team = models.CharField(max_length=100, verbose_name="Team Name")
    team_manager  = models.CharField(max_length=100, verbose_name="Team Manager")

    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.team

