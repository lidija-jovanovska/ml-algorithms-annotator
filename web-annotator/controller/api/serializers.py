from rest_framework import serializers
from .models.dm_algorithm import Algorithm

class AlgorithmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Algorithm
        fields = ('node_id', 'name')