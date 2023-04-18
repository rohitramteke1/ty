from django.db import models

# Create your models here.
from ckeditor.fields import RichTextField
class Editor(models.Model):
    body=RichTextField(blank=True,null=True)