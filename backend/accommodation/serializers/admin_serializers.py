from rest_framework.serializers import ModelSerializer

from accommodation.models import Property
from accommodation.serializers.public_serializers import (
    PublicPropertyImageSerializer,
)


class AdminPropertyImageSerializer(PublicPropertyImageSerializer):
    class Meta(PublicPropertyImageSerializer.Meta):
        fields = (
            "id",
            "photo_url",
            "order",
        )


class AdminPropertySerializer(ModelSerializer):
    images = AdminPropertyImageSerializer(many=True, read_only=False)

    class Meta:
        model = Property
        fields = (
            "id",
            "name",
            "slug",
            "address",
            "description",
            "images",
        )


# {
#     "id": 1,
#     "name": "Forest House",
#     "slug": "forest-house",
#     "address": "...",
#     "description": "...",
#     "images": [
#         {
#             "id": 1,
#             "photo_url": "https://...",
#             "order": 0
#         },
#         {
#             "id": 2,
#             "photo_url": "https://...",
#             "order": 1
#         },
#         {
#             "id": 3,
#             "photo_url": "https://...",
#             "order": 2
#         }
#     ]
# }
