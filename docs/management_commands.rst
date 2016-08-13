Management commands
===================

Add some feeds:

.. code-block:: python

    python manage.py planet_add_feed https://www.djangoproject.com/rss/weblog/
    python manage.py planet_add_feed https://djangopackages.org/feeds/packages/latest/rss/
    
Update a feed:

.. code-block:: python

	python manage.py planet_update_feed https://www.djangoproject.com/rss/weblog/
	
Update all the feeds:

.. code-block:: python

	python manage.py planet_update_all_feeds
	
Empty all feeds:

.. code-block:: python

	python manage.py planet_flush_all_feeds