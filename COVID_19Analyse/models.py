from django.db import models


# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=20, unique=True)
    continent = models.CharField(max_length=5, default="亚洲")

    def __str__(self):
        return self.name

    class Meta:
        indexes = [models.Index(fields=['continent']), ]


class CountryData(models.Model):
    date = models.DateField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE, default="")
    confirm_add = models.IntegerField(default=0)
    confirm = models.IntegerField(default=0)
    heal = models.IntegerField(default=0)
    dead = models.IntegerField(default=0)

    def __str__(self):
        return str(self.country) + " " + self.date.strftime("%Y/%m/%d")

    class Meta:
        indexes = [models.Index(fields=['country']),models.Index(fields=['date']),models.Index(fields=['country','date']), ]

