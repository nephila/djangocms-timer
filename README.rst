===============
djangocms-timer
===============

.. image:: https://pypip.in/v/djangocms-timer/badge.png
        :target: https://pypi.python.org/pypi/djangocms-timer
        :alt: Latest PyPI version

.. image:: https://travis-ci.org/nephila/djangocms-timer.png?branch=master
        :target: https://travis-ci.org/nephila/djangocms-timer
        :alt: Latest Travis CI build status

.. image:: https://pypip.in/d/djangocms-timer/badge.png
        :target: https://pypi.python.org/pypi/djangocms-timer
        :alt: Monthly downloads

.. image:: https://coveralls.io/repos/nephila/djangocms-timer/badge.png
        :target: https://coveralls.io/r/nephila/djangocms-timer
        :alt: Test coverage

django CMS plugin that shows content between specified times

Documentation
-------------

The full documentation is at https://djangocms-timer.readthedocs.org.

Quickstart
----------

Install djangocms-timer::

    pip install djangocms-timer


Features
--------

Shows and hides child plugins according to the timers set in the plugin instance.

Caveats
-------

In its current form, plugin won't save you from the queries to retrieve child
plugins due to the way plugin rendering works in django CMS. Still, the
``render`` method of child plugins is not executed (and grandchildren plugins
are not retrieved) with mitigating effect on performance hit.
