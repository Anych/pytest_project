from rest_framework import seriazlizers
from .models import Company


class CompanySerializer(seriazlizers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name', 'status', 'application_link', 'last_update', 'notes']