from rest_framework import serializers
from testAPI.models import CaffeModel


class CaffeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaffeModel 
        fields = '__all__'
        # fields = ('id', 'song', 'singer', 'last_modify_date', 'created')
