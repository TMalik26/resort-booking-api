from dj_rest_auth.serializers import LoginSerializer
from rest_framework import serializers


class CustomLoginSerializer(LoginSerializer):
    username = None  # Disable username field
    email = serializers.EmailField(required=True)
