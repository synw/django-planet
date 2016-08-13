#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand

from planet.tasks import process_feed
from planet.settings import ASYNC_BACKEND


class Command(BaseCommand):
    help = "Update a feed."
    args = "<feed_url>"

    def handle(self, *args, **options):
        if not len(args):
            print("You must provide the feed url as parameter")
            exit(0)

        feed_url = args[0]
        # process feed in create-mode
        if ASYNC_BACKEND == "celery":
            process_feed.delay(feed_url, create=False)
        elif ASYNC_BACKEND == "huey":
            from planet.tasks import huey_process_feed
            huey_process_feed(feed_url, create=False)
        else:
            process_feed(feed_url, create=False)
