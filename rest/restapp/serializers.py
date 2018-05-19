from rest_framework import serializers

from restapp.models import CurrencyRates


class CurrencyRatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrencyRates
        # fields = ('name', 'rate', 'updated')
        fields = '__all__'