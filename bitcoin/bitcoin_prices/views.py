from bitcoin_prices.models import CurrentPrices, Prices
from django.db.models import Avg, Max, Min
from django.shortcuts import HttpResponse, render
import GDAX


# Create your views here.


def index(request):
    return HttpResponse("Welcome to Bitcoin Prices")


def prices(request):
    publicClient = GDAX.PublicClient()
    stats = publicClient.getProduct24HrStats()
    last_price = Prices.objects.create(last_price=float(stats["last"]))
    last_ten = CurrentPrices.objects.all().order_by("-created")[:10]
    average_price = last_ten.aggregate(Avg("current_price"))["current_price__avg"]
    min_price = last_ten.aggregate(Min("current_price"))["current_price__min"]
    high_price = last_ten.aggregate(Max("current_price"))["current_price__max"]

    return render(request, "bitcoin_prices/prices.html", {
        "last_price": last_price,
        "last_ten": last_ten,
        "average_price": average_price,
        "min_price": min_price,
        "high_price": high_price})
