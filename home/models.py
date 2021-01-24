from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.search import index
from wagtail.documents.models import Document, AbstractDocument




class HomePage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname='full'),
    ]
    def get_context(self, request):
        context = super().get_context(request)

        # Add extra variables and return the updated context
        context[''] = HomePage.objects.child_of(self).live()
        return context

    subpage_types = ['home.ContentPage','FAQPage']


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

class ContentPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname='full'),
    ]
    def get_context(self, request):
        context = super().get_context(request)

        # Add extra variables and return the updated context
        context[''] = ContentPage.objects.child_of(self).live()
        return context

    subpage_types = ['home.BookPage','StandartPage']


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
    parent_page_types = ['home.ContentPage']


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
    parent_page_types = ['home.ContentPage']

