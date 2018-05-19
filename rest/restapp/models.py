from django.db import models

# Create your models here.
class CurrencyRates(models.Model):
    name = models.CharField(max_length=50)
    rate = models.FloatField()
    updated = models.DateTimeField()

    class Meta:
        verbose_name = "CurrencyRates"

    def __unicode__(self):
        return self.name