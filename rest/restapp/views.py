from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from restapp.models import CurrencyRates
from restapp.serializers import CurrencyRatesSerializer

@api_view(['GET'])
def get_currencies(request):
    try:
        rates = CurrencyRates.objects.all()
    except CurrencyRates.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CurrencyRatesSerializer(rates, many=True)
        return Response(serializer.data)