from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.search import index
from wagtail.documents.models import Document, AbstractDocument


class HomePage(Page):
    pass

class FAQPage(Page):
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        FieldPanel('body', classname="full"),
    ]

class BookPage(Page):
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)
    date = models.DateField("Post date")
    author = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    admin_form_fields = Document.admin_form_fields + (
        'author',
    )

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
        index.SearchField('author'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        FieldPanel('body', classname="full"),
        FieldPanel('date'),
        FieldPanel('author'),
    ]


class StandartPage(Page):
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)
    date = models.DateField("Post date")
    author = models.CharField(
        max_length=255
        blank=True,
        null=True
    )

    admin_form_fields = Document.admin_form_fields + (
        'author',
    )

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
        index.SearchField('author'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        FieldPanel('body', classname="full"),
        FieldPanel('date'),
        FieldPanel('author'),
    ]

