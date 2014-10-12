#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import djangocms_timer

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = djangocms_timer.__version__

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='djangocms-timer',
    version=version,
    description="""django CMS plugin that shows content between specified times""",
    long_description=readme + '\n\n' + history,
    license='GPLv2+',
    author='Iacopo Spalletti',
    author_email='i.spalletti@nephila.it',
    url='https://github.com/nephila/djangocms-timer',
    packages=[
        'djangocms_timer',
    ],
    include_package_data=True,
    install_requires=[
        'django-cms>=3.0'
    ],
    zip_safe=False,
    keywords='djangocms-timer',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
)