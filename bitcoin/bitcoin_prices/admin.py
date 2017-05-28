from django.contrib import admin
from bitcoin_prices.models import Prices, CurrentPrices

# Register your models here.


@admin.register(Prices)
class PricesAdmin(admin.ModelAdmin):
    list_display = ("last_price", )


@admin.register(CurrentPrices)
class CurrentPricesAdmin(admin.ModelAdmin):
    list_display = ("current_price", )
