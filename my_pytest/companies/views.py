from django.shortcuts import render

class CompanyViewSet(ModelViewSet):
    serializer_class = CompanySerializer
