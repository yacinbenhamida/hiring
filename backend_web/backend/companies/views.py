from django.shortcuts import render
from .serializers import CompaniesSerializer, MatchesSerializer
from .models import Companies, Matches
from rest_framework import viewsets, generics
from django.http import HttpResponse, JsonResponse
from django.db.models import Q

class CompaniesView(viewsets.ModelViewSet):
    queryset = Companies.objects.all().order_by('name')
    serializer_class = CompaniesSerializer
class CompanyMatching(generics.ListAPIView):
    serializer_class = MatchesSerializer
    pagination_class = None
    def get_queryset(self):
        company = self.kwargs['company']
        return Matches.objects.filter(Q(left_company_id=company) | Q(right_company_id=company))