from django.forms import ModelForm
from .models import Project

# create a form based on the Project model in models.py
class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = [
            'title',
            'featured_image',
            'description',
            'demo_link',
            'source_link',
            'tags'
        ]