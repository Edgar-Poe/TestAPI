from django.core.management.base import BaseCommand
from articles.models import Vote


class Command(BaseCommand):

    def handle(self, *args, **options):

        Vote.objects.all().delete()
