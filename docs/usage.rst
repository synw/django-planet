Usage
=====

.. toctree::
  :maxdepth: 1
  :hidden:

  install

  screenshots
  demo
  
  contributing

Management commands
-------------------

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
	
Auto update
-----------

There are 2 options to auto update the feeds:

1. Use a cron job:

    30 * * * * python manage.py planet_update_all_feeds

This attempts to pull in new posts every 30 minutes.

2. Use an async time based worker (Celery or Huey):

* Celery:

Install Celery ``pip install celery redis``. You will need a ``celery.py`` file 
as explained `here <http://docs.celeryproject.org/en/latest/django/first-steps-with-django.html>`_. A Redis 
or RabbitMQ instance is also required, check the Celery docs.
In settings.py:

.. code-block:: python

    from datetime import timedelta
	CELERYBEAT_SCHEDULE = {
	    'update-feeds': {
	        'task': 'planet.tasks.update_feeds',
	        'schedule': timedelta(minutes=30),
	    },
	}
 

* Huey

Install Celery ``pip install huey``. Add ``huey.contrib.djhuey`` in INSTALLED_APPS.
In settings.py:

.. code-block:: python

    ASYNC_BACKEND = "huey"
    
    from huey import RedisHuey
    HUEY = RedisHuey('your_project_name')
	
Then launch the worker. For Celery start a beat and a worker:

.. code-block:: python

    celery -A project_name beat  -l info --broker='redis://localhost:6379/0'
    celery -A project_name worker  -l info --broker='redis://localhost:6379/0'
	
For Huey:

.. code-block:: python

    python manage.py run_huey


