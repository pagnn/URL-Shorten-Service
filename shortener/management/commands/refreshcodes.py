from django.core.management.base import BaseCommand, CommandError

from shortener.models import UssURL

class Command(BaseCommand):
    help = 'Refresh all current url shortcodes'
    def add_arguments(self,parser):
        parser.add_argument('--items',type=int)

    def handle(self, *args, **options):
        return UssURL.objects.refresh_shortcodes(options['items'])