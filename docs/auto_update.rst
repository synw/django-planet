Setup auto updates
==================

By default auto updates are not enabled.

There are 2 options to set auto update for the feeds: a cron job or an async job.

Cron job
--------

    30 * * * * python manage.py planet_update_all_feeds

This attempts to pull in new posts every 30 minutes.

Celery
------

Install Celery ``pip install celery redis``. You will need a ``celery.py`` file 
as explained `here <http://docs.celeryproject.org/en/latest/django/first-steps-with-django.html>`_. A Redis 
or RabbitMQ instance is also required, check the Celery docs.
In settings.py:

.. code-block:: python

	PLANET_ASYNC_BACKEND = "celery"

    from datetime import timedelta
	CELERYBEAT_SCHEDULE = {
	    'update-feeds': {
	        'task': 'planet.tasks.update_feeds',
	        'schedule': timedelta(minutes=30),
	    },
	}
	
Then launch the worker: start a beat and a worker:

.. code-block:: python

    celery -A project_name beat  -l info --broker='redis://localhost:6379/0'
    celery -A project_name worker  -l info --broker='redis://localhost:6379/0'
 

Huey
----

Huey is easier to configure than Celery. If you are not familiar with Celery you might want to use 
it for an easy start.

Install Huey: ``pip install huey``. Add ``huey.contrib.djhuey`` in INSTALLED_APPS.
In settings.py:

.. code-block:: python

    PLANET_ASYNC_BACKEND = "huey"
    
    from huey import RedisHuey
    HUEY = RedisHuey('your_project_name')
	
Launch the worker:

.. code-block:: python

    python manage.py run_huey


