# -*- coding: utf-8 -*-
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.timezone import now
from django.utils.translation import ugettext_lazy as _

from .models import TimerPluginModel


class TimerContainerPlugin(CMSPluginBase):
    name = _(u'Timed content')
    model = TimerPluginModel
    allow_children = True
    cache = False
    render_template = 'djangocms_timer/timer.html'

    def render(self, context, instance, placeholder):
        if instance.date_publish <= now() and (instance.date_publish_end is None or instance.date_publish_end > now()):
            context['instance'] = instance
        return context
plugin_pool.register_plugin(TimerContainerPlugin)
