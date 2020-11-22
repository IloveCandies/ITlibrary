from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.search import index
from wagtail.documents.models import Document, AbstractDocument


class HomePage(Page):
    pass

class Book(Page):
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)
    date = models.DateField("Post date")
    source = models.CharField(
        max_length=255,
        # This must be set to allow Wagtail to create a document instance
        # on upload.
        blank=True,
        null=True
    )

    admin_form_fields = Document.admin_form_fields + (
        # Add all custom fields names to make them appear in the form:
        'source',
    )

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
        index.SearchField('source'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        FieldPanel('body', classname="full"),
        FieldPanel('date'),
        FieldPanel('source'),
    ]
