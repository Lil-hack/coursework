import uuid

from django.db import models
from pygments import highlight
from pygments.formatters.html import HtmlFormatter
from pygments.lexers import get_all_lexers, get_lexer_by_name
from pygments.styles import get_all_styles
import hashlib


def make_password(password):
    assert password
    hash = hashlib.md5(password.encode('utf-8')).hexdigest()
    return hash



class Users(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    uuid=models.UUIDField(primary_key=True,unique=True, default='42265564-4a78-4e14-84fc-0d1da2075440')
    username = models.TextField(unique=True)
    first_name = models.TextField()
    last_name = models.TextField()
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField( default=False)
    password = models.TextField()

    class Meta:
        ordering = ('created', )

    def save(self, *args, **kwargs):
        """
        Use the `pygments` library to create a highlighted HTML
        representation of the code snippet.
        """
        if self._state.adding:
            self.uuid=uuid.uuid4()
            self.password=make_password(self.password)
        super(Users, self).save(*args, **kwargs)

