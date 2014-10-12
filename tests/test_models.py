# -*- coding: utf-8 -*-
from datetime import timedelta
from django.template import RequestContext
from django.utils.encoding import force_text
from django.utils.timezone import now
from django.utils.translation import ugettext_lazy as _
from cms.api import add_plugin
from cms.plugin_rendering import render_placeholder
from djangocms_helper.test_base import BaseTestCase


class TestPlugin(BaseTestCase):
    _pages_data = (
        {'en': {'title': 'Page title', 'template': 'page.html', 'publish': True},
         'fr': {'title': 'Titre', 'publish': True},
         'it': {'title': 'Titolo pagina', 'publish': False}},
    )

    def test_basic_context_setup(self):
        page1, = self.get_pages()
        ph = page1.placeholders.get(slot='content')
        date_start = now()

        plugin_data = {
            'date_publish': date_start
        }
        plugin = add_plugin(ph, 'TimerContainerPlugin', language='en', **plugin_data)
        instance, plugin_class = plugin.get_plugin_instance()
        request = self.get_page_request(page1, self.user, r'/en/', lang='en')
        context = RequestContext(request, {})
        pl_context = plugin_class.render(context, instance, ph)
        self.assertTrue('instance' in pl_context)
        self.assertEqual(pl_context['instance'], instance)
        self.assertEqual(force_text(instance),
                         _(u'Start publish at %(start)s') %
                         {'start': date_start})

        plugin_data = {
            'date_publish': date_start,
            'date_publish_end': date_start + timedelta(seconds=10)
        }
        plugin = add_plugin(ph, 'TimerContainerPlugin', language='en', **plugin_data)
        instance, plugin_class = plugin.get_plugin_instance()
        request = self.get_page_request(page1, self.user, r'/en/', lang='en')
        context = RequestContext(request, {})
        pl_context = plugin_class.render(context, instance, ph)
        self.assertTrue('instance' in pl_context)
        self.assertEqual(pl_context['instance'], instance)
        self.assertEqual(force_text(instance),
                         _(u'Start publish at %(start)s - End at %(end)s') %
                         {'start': date_start, 'end': date_start + timedelta(seconds=10)})

        plugin_data = {
            'date_publish': date_start + timedelta(days=1)
        }
        plugin = add_plugin(ph, 'TimerContainerPlugin', language='en', **plugin_data)
        instance, plugin_class = plugin.get_plugin_instance()
        request = self.get_page_request(page1, self.user, r'/en/', lang='en')
        context = RequestContext(request, {})
        pl_context = plugin_class.render(context, instance, ph)
        self.assertFalse('instance' in pl_context)

        plugin_data = {
            'date_publish': date_start - timedelta(days=1),
            'date_publish_end': date_start - timedelta(seconds=10)
        }
        plugin = add_plugin(ph, 'TimerContainerPlugin', language='en', **plugin_data)
        instance, plugin_class = plugin.get_plugin_instance()
        request = self.get_page_request(page1, self.user, r'/en/', lang='en')
        context = RequestContext(request, {})
        pl_context = plugin_class.render(context, instance, ph)
        self.assertFalse('instance' in pl_context)

    def test_children_shown(self):
        page1, = self.get_pages()
        ph = page1.placeholders.get(slot='content')
        date_start = now()

        text_content = u"Child plugin"

        plugin_data = {
            'date_publish': date_start
        }
        plugin_1 = add_plugin(ph, 'TimerContainerPlugin', language='en', **plugin_data)
        plugin_1.save()

        # child of plugin_1
        plugin_2 = add_plugin(ph, u"TextPlugin", u"en", body=text_content)
        plugin_1 = self.reload_model(plugin_1)
        plugin_2.parent = plugin_1
        plugin_2.save()

        request = self.get_page_request(page1, self.user, r'/en/', lang='en')
        context = RequestContext(request, {})
        content = render_placeholder(ph, context)
        self.assertEqual(content, text_content)

    def test_children_hidden(self):
        page1, = self.get_pages()
        ph = page1.placeholders.get(slot='content')
        date_start = now()

        text_content = u"Child plugin"

        plugin_data = {
            'date_publish': date_start + timedelta(days=1),
        }
        plugin_1 = add_plugin(ph, 'TimerContainerPlugin', language='en', **plugin_data)
        plugin_1.save()

        # child of plugin_1
        plugin_2 = add_plugin(ph, u"TextPlugin", u"en", body=text_content)
        plugin_1 = self.reload_model(plugin_1)
        plugin_2.parent = plugin_1
        plugin_2.save()

        request = self.get_page_request(page1, self.user, r'/en/', lang='en')
        context = RequestContext(request, {})
        content = render_placeholder(ph, context)
        self.assertEqual(content, '')
