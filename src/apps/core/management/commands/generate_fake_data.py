from django.core.management.base import BaseCommand
from apps.core.factories import ShoeFactory
from apps.accounts.factories import UserFactory


class Command(BaseCommand):
    help = 'Generates fake data'

    def add_arguments(self, parser):
        parser.add_argument('--number',
            default=50,
            type=int,
            help='The number of fake instances do create.')

    def handle(self, *args, **options):
        amount = options['number']
        UserFactory.create_batch(amount)
        ShoeFactory.create_batch(amount)

