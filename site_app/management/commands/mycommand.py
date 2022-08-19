from django.core.management.base import BaseCommand
from ...models_data import WeatherData, YieldData, Results


class Command(BaseCommand):
    def handle(self, *args, **options):
        WeatherData()
        YieldData()
        Results()
