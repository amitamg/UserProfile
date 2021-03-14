from rest_framework import serializers
from .models import CintaUser
import json


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CintaUser
        fields = ['username', 'age', 'skills', 'image1', 'image2']

    def validate_meta_data(self, data):
        try:
            data = json.loads(data)
            return data
        except json.JSONDecodeError:
            raise serializers.ValidationError("Invalid JSON payload")

