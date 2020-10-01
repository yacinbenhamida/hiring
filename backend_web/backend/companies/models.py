from django.db import models

class Companies(models.Model):
    id = models.IntegerField(primary_key=True)
    source_id = models.IntegerField()
    source_name = models.CharField(max_length=64)
    name = models.CharField(max_length=512)
    email = models.CharField(max_length=512)
    phone = models.CharField(max_length=512,null=True)
    address = models.CharField(max_length=512)
    postal_code = models.CharField(max_length=512)
    city = models.CharField(max_length=512)
    website = models.CharField(max_length=512)
    country = models.CharField(max_length=512)
    class Meta:
        db_table = "companies"
    def __str__(self):
        return self.name

class Matches(models.Model):
    id = models.IntegerField(primary_key=True)
    left_company_id = models.ForeignKey(Companies, on_delete=models.CASCADE, 
                                        null=False, related_name='left_company')
    right_company_id = models.ForeignKey(Companies, on_delete=models.CASCADE, 
                                         null=False, related_name='right_company')
    class Meta:
        db_table = "matches"