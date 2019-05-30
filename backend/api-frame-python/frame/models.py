import uuid

from django.db import models
from pygments import highlight
from pygments.formatters.html import HtmlFormatter
from pygments.lexers import get_all_lexers, get_lexer_by_name
from pygments.styles import get_all_styles



class Frame(models.Model):
    id = models.BigAutoField(primary_key=True, unique=True)
    video_uuid=models.TextField()
    hash = models.TextField()
    frame = models.IntegerField()

    class Meta:
        ordering = ( )


    def save(self, *args, **kwargs):
        """
        Use the `pygments` library to create a highlighted HTML
        representation of the code snippet.
        """

        super(Frame, self).save(*args, **kwargs)


class Photo(models.Model):
    id = models.TextField(primary_key=True, unique=True)
    title = models.TextField()

    def __str__(self):
        return self.file.name
