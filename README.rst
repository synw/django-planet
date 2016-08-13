=============
Django Planet
=============

This is a generic application for Django projects aiming to provide a planet
feed aggregator app.

Note: this fork makes this app compatible with modern versions of Django and continues the development. 

Installation
============

For installation instructions, see `the docs <http://django-planet-continued.readthedocs.io/en/latest/install.html>`_.
    
Note for Django 1.9 : you have to clone the `django-pagination-py3 repository <https://github.com/matagus/django-pagination-py3>`_ as
the pip version is not yet compatible with Django 1.9.

Demo
====

There is a `simple demo django-planet <http://django-planet.com/>`_.


Todo
====

- Fix the tests with reversed urls
- Improve the search (and remove the context processor)
- Categories refactoring using mptt
- Feeds management in a GUI

License
=======

The project is licensed under the BSD license.


