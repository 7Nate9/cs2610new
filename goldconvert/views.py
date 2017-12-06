# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

from models import conversionFactor

# Create your views here.
def conversion(request, fromUnit, toUnit, weight):
    fromConversion = conversionFactor.objects.get(unit=fromUnit)
    fromFactor = fromConversion.factor
    
    toConversion = conversionFactor.objects.get(unit=toUnit)
    toFactor = toConversion.factor
    
    endWeight = weight * fromFactor / toFactor
    response = HttpResponse()
    response['endWeight'] = endWeight
    
    return response