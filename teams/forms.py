from django import forms
from .models import Team
class TeamForm(forms.ModelForm):
    team = forms.CharField(label="Team",max_length=100)
    team_manager = forms.CharField(label="Team Manager",max_length=100)

    class Meta:
        model = Team
        exclude = ("created_by",)