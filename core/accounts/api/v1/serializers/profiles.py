from rest_framework import serializers
from ....models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    email = serializers.CharField(source="user.email", read_only=True)

    class Meta:
        model = Profile
        fields = [
            "id",
            "user",
            "email",
            "first_name",
            "last_name",
            "image",
            "description",
        ]
        read_only_fields = ["user"]
