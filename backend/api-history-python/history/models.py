import uuid

from django.db import models
from pygments import highlight
from pygments.formatters.html import HtmlFormatter
from pygments.lexers import get_all_lexers, get_lexer_by_name
from pygments.styles import get_all_styles



class History(models.Model):

    uuid=models.UUIDField(primary_key=True,unique=True, default='42265564-4a78-4e14-84fc-0d1da2075440')
    user_uuid = models.UUIDField()
    video_uuid = models.TextField()
    created = models.DateField(auto_now_add=True)
    url_search_foto = models.TextField()
    url_find_foto = models.TextField()


    class Meta:
        ordering = ('created', )


    def save(self, *args, **kwargs):
        """
        Use the `pygments` library to create a highlighted HTML
        representation of the code snippet.
        """
        if self._state.adding:
            self.uuid=uuid.uuid4()

        super(History, self).save(*args, **kwargs)

