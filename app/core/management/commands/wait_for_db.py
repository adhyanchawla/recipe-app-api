"""
Django command to wait for the database to be available.
"""
import time
from psycopg2 import OperationalError as Psycopg2Error
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand
from django.db import connections

class Command(BaseCommand):
    """Django  command to wait for database."""

    def handle(self, *args, **options):
        """Entrypoint for command"""
        self.stdout.write('Waiting for database')
        db_conn = None
        while db_conn is None:
            try:
                db_conn = connections['default']
            except (Psycopg2Error, OperationalError):
                self.stdout.write('Database Unavailable, waiting 1 second...')
                time.sleep(1)
        
        self.stdout.write(self.style.SUCCESS('Database Available!'))