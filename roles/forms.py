from django import forms
from .models import Role

class RoleForm(forms.ModelForm):
    role = forms.CharField(label="Role",max_length=100)
    team = forms.CharField(label="Team",max_length=100)

    class Meta:
        model = Role
        exclude = ("created_by",)