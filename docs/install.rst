Install
=======

``pip install django-planet``

Required settings
-----------------

Modify your projects ``settings.py`` file following the next steps:

In ``INSTALLED_APPS``:

.. code-block:: python

    'pagination',
    'tagging',
    'planet',

Be sure to set the site id:

.. code-block:: python

  SITE_ID = 1

Include the context processor:

.. code-block:: python

    TEMPLATE_CONTEXT_PROCESSORS = (
        #...
        'planet.context_processors.context',
    )

Add the pagination middleware:

.. code-block:: python

    MIDDLEWARE_CLASSES = (
        # ...
        'pagination.middleware.PaginationMiddleware',
    )

Urls
----

In ``urls.py``:

.. code-block:: python

    urlpatterns = patterns('',
    	# ...
        url(r'^planet/^', include('planet.urls')),
    )

Optional settings
-----------------

To modify cookie names so you don’t have login conflicts with other projects:

.. code-block:: python

    LANGUAGE_COOKIE_NAME = "myplanetlng"
    SESSION_COOKIE_NAME = "myplanetid"
	
Select the async backend:

.. code-block:: python

    ASYNC_BACKEND = "huey"

This will be detailed in the next section.



