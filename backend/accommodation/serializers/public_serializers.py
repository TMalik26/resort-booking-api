from rest_framework.serializers import ModelSerializer, SerializerMethodField

from accommodation.models import Property, PropertyImage
from storage.services import get_public_supabase_url


class PublicPropertyImageSerializer(ModelSerializer):
    photo_url = SerializerMethodField()

    class Meta:
        model = PropertyImage
        fields = (
            "id",
            "photo_url",
        )

    def get_photo_url(self, obj):
        """Return the public URL for the image stored in Supabase."""
        return get_public_supabase_url(obj.image)


class PublicPropertySerializer(ModelSerializer):
    images = PublicPropertyImageSerializer(many=True, read_only=True)

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
#         },
#         {
#             "id": 2,
#             "photo_url": "https://...",
#         },
#         {
#             "id": 3,
#             "photo_url": "https://...",
#         }
#     ]
# }
