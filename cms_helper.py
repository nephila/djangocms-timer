# -*- coding: utf-8 -*-
import sys
from tempfile import mkdtemp
gettext = lambda s: s

HELPER_SETTINGS = {
    'NOSE_ARGS': [
        '-s',
    ],
    'INSTALLED_APPS': [
        'djangocms_text_ckeditor',
    ],
    'LANGUAGE_CODE': 'en',
    'LANGUAGES': (
        ('en', gettext('English')),
        ('it', gettext('Italiano')),
    ),
    'CMS_LANGUAGES': {
        1: [
            {
                'code': 'en',
                'name': gettext('English'),
                'public': True,
            },
            {
                'code': 'it',
                'name': gettext('Italiano'),
                'public': True,
            },
        ],
        'default': {
            'hide_untranslated': False,
        },
    },
    'MIDDLEWARE_CLASSES': [
        'django.contrib.messages.middleware.MessageMiddleware',
    ],
    'SITE_ID': 1
}
if 'test' in sys.argv:
    HELPER_SETTINGS['INSTALLED_APPS'].append('django_nose')