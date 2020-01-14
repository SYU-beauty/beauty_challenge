from django.db import models

# Create your models here.
class Item(models.Model):
    fixtures = ['items-data.json', 'item']
    name = models.CharField(max_length=32)
    quantity = models.IntegerField()

{"id":1,"imageId":"a18de8cd-c730-4f36-b16f-665cca908c11",
"name":"리더스 링클 콜라겐 마스크",
"price":"520",
"gender":"female",
"category":"suncare",
"ingredients":"executrix,provision,multimedia,destruction,screw",
"monthlySales":5196}