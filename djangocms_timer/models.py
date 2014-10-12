# -*- coding: utf-8 -*-
from cms.models import CMSPlugin
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.timezone import now
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class TimerPluginModel(CMSPlugin):
    date_publish = models.DateTimeField(_(u'Start publishing at'), default=now)
    date_publish_end = models.DateTimeField(_(u'End publishing at'), null=True, blank=True)

    def __str__(self):
        if self.date_publish_end:
            return _(u'Start publish at %(start)s - End at %(end)s') % {'start': self.date_publish,
                                                                        'end': self.date_publish_end}
        else:
            return _(u'Start publish at %(start)s') % {'start': self.date_publish}
