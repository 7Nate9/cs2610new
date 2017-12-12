# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from models import conversionFactor

# Create your views here.
def conversion(request):
    fromUnit = request.GET['from']
    toUnit = request.GET['to']
    weight = float(request.GET['value'])
    
    fromConversion = conversionFactor.objects.get(unit=fromUnit)
    fromFactor = fromConversion.factor
    
    toConversion = conversionFactor.objects.get(unit=toUnit)
    toFactor = toConversion.factor
    
    endWeight = weight * fromFactor / toFactor
    print(endWeight)
    response = JsonResponse({'unit':toUnit, 'value':endWeight})
    
    return response