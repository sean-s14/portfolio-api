from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from markdownx.models import MarkdownxField
from django.utils.text import slugify

class Article(models.Model):
    title        = models.CharField(unique=True, blank=False, null=False, max_length=60)
    slug         = models.SlugField(unique=True, blank=True, null=True, max_length=60)
    imageURI     = models.TextField(blank=False, null=False)
    text         = MarkdownxField()
    date_created = models.DateTimeField(_("date created"), default=timezone.now)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)