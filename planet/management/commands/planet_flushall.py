#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand

from planet.models import Feed


class Command(BaseCommand):
    help = "Flushes all feeds."

    def handle(self, *args, **options):
        feeds = Feed.objects.all()
        for feed in feeds:
            print "Deleting feed "+feed.title
            feed.delete()
        return
