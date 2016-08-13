# -*- coding: utf-8 -*-
from django.core.management.base import NoArgsCommand

from planet.tasks import process_feed
from planet.models import Feed
from planet.signals import feeds_updated
from planet.settings import ASYNC_BACKEND


class Command(NoArgsCommand):
    help = "Update all feeds"

    def handle(self, *args, **options):
        for feed_url in Feed.site_objects.all().values_list("url", flat=True):
            if ASYNC_BACKEND == "celery":
                self.stdout.write("Scheduling feed with URL=%s..." % feed_url)
                process_feed.delay(feed_url, create=False)
            elif ASYNC_BACKEND == "huey":
                from planet.tasks import huey_process_feed
                huey_process_feed(feed_url, create=False)
            else:
                process_feed(feed_url, create=False)

        feeds_updated.send(sender=self, instance=self)
        return
