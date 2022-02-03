from django.db import models
from markdownx.models import MarkdownxField
# Create your models here.

class Blog(models.Model):
    # date = models.DateField()
    created_at = models.DateField('作成日', auto_now_add=True)
    updated_at = models.DateField('更新日', auto_now=True)
    title = models.CharField("title", max_length=255)
    contents = MarkdownxField()
    
    def __str__(self):
        return self.title