from django.shortcuts import render
from .serializers import CompaniesSerializer, CompanyDetailsSerializer
from .models import Companies, Matches
from rest_framework import viewsets
from django.http import HttpResponse, JsonResponse
# Create your views here.

class CompaniesView(viewsets.ModelViewSet):
    queryset = Companies.objects.all().order_by('name')
    serializer_class = CompaniesSerializer
    
def companies_details(request,pk):
    try:
        company = Companies.objects.get(pk=pk)
    except Companies.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        serializer = CompanyDetailsSerializer(company)
        return JsonResponse(serializer.data) 
