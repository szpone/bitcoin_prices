from bitcoin_prices.models import CurrentPrices
from django.core.management import BaseCommand
import GDAX
import time


class Command(BaseCommand):
    help = "This command allows to get current data from GDAX API"

    def handle(self, *args, **options):
        publicClient = GDAX.PublicClient()
        stats = publicClient.getProduct24HrStats()
        while True:
            CurrentPrices.objects.create(current_price=float(stats['last']))
            time.sleep(60)
