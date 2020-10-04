from rest_framework import serializers
from .models import Companies,Matches

class CompaniesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Companies
        fields = ('id','name', 'source_name','source_id','email',
                  'phone','postal_code','city','country','address') 
class MatchesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Matches
        fields = ('id','left_company_id', 'right_company_id')
        depth = 1   