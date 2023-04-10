from django.core.management.base import BaseCommand, CommandError
from neomodel import db

class Command(BaseCommand):
    help = 'Wipe whole database (taxonomies and algorithms).'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        try:
            db.cypher_query("MATCH (n) OPTIONAL MATCH (n)-[r]-() DELETE n,r")
            self.stdout.write(self.style.SUCCESS('Successfully wiped database.'))
        except Exception as e:
            raise CommandError('Error while wiping database: %s' % e)