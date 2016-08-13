.. django-planet documentation master file, created by
   sphinx-quickstart on Sun Jan 12 14:07:23 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Django Planet
=============

This is a generic application for Django that allows you to quickly build a
planet aggregating RSS and ATOM feeds.

.. image:: _static/screenshots/latest-posts.png

Some parts of this help docs has been copied from `django-tastypie`_ and then
readapted to django-planet. Kudos to `django-tastypie`_ for its docs!

.. _`django-tastypie`: http://groups.google.com/toastdriven/django-tastypie/

Content:
--------

.. toctree::
  :maxdepth: 2

  install
  auto_update
  management_commands
  
  screenshots
  demo
  contributing


Requirements
============

django-planet requires the following modules but simply installing it
using Pip_ will also install them: ``pip install django-planet``

Required
--------

* Python 2.6+
* Django 1.6/1.7
* django-tagging 0.3.6
* django-pagination 1.0.0+
* feedparser
* BeautifulSoup4

Optionally, install celery if you want to add and update feeds using async &
parallel tasks:

* Celery or Huey

Why django-planet?
==================

There are other feed aggregators out there for Django. You need to assess
the options available and decide for yourself. That said, here are some
common reasons for django-planet.

* You need to quickly create a blog aggregator website with a nice look & feel.
* You want a full website for browsing blog posts and its authors and tags,
  feeds and blogs.
* SEO matters to you: django-planet has templates with SEO metatags and it
  includes sitemaps so you may submit them to your favorite search engines.
* You want searching posts, blogs, tags and authors.
* You need to customize templates and have a rich set of template tags to do it.
* You want complete ATOM & RSS support

Running The Tests
=================

The easiest way to get setup to run django-planet's tests looks like::

  $ git clone https://github.com/matagus/django-planet.git
  $ cd django-planet
  $ virtualenv env
  $ . env/bin/activate
  $ ./env/bin/pip install -U -r requirements.txt
  $ ./env/bin/pip install -U mock django-discover-runner factory-boy tox

Then running the tests is as simple as::

  # From the same directory as above:
  $ tox

That will test django-planet using Python 2.7 combinated with Django 1.4,
Django 1.5 and Django 1.6.


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
