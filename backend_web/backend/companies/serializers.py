from rest_framework import serializers
from .models import Companies,Matches

class CompaniesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Companies
        fields = ('id','name', 'source_name')
class CompanyDetailsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Companies
        fields = ('id','name', 'source_name','source_id','email',
                  'phone','postal_code','city','country','address')   