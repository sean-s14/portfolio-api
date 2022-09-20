from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.utils.text import slugify


class Project(models.Model):

    class Category(models.TextChoices):
        JS = "JS", "JAVASCRIPT"
        RC = "RC", "REACT"
        RCN = "RCN", "REACT NATIVE"
        HTML = "HTML", "HTML"
        CSS = "CSS", "CSS"
        SASS = "SASS", "SASS"
        PY = "PY", "PYTHON"
        DJ = "DJ", "DJANGO"
        DJR = "DJR", "DJANGO REST"


    imageURI     = models.TextField()
    title        = models.CharField(unique=True, blank=False, null=False, max_length=150)
    slug         = models.SlugField(unique=True, blank=True, null=True, max_length=60)
    category     = models.CharField(max_length=4, choices=Category.choices, blank=False, null=False)
    link         = models.URLField(unique=True, blank=True, null=True, max_length=150)
    description  = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(_("date created"), default=timezone.now)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)