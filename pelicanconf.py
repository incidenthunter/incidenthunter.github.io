#!/usr/bin/env python
# -*- coding: utf-8 -*- #

from __future__ import unicode_literals
import os

AUTHOR = u'Incident Hunter'
SITENAME = u'We are now in the decade of response'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
THEME = 'ghastly'
DIRECT_TEMPLATES = (('index', 'archives', '404'))

PLUGIN_PATHS = [ os.path.join(os.environ['HOME'], 'third-party', 'pelican-plugins')]
PLUGINS = ['assets', 'sitemap', 'gravatar']
