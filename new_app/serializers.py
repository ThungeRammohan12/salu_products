from rest_framework import serializers
from .models import SaluProduct

class SaluProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaluProduct
        fields = '__all__'
