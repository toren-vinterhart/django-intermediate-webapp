from django.shortcuts import get_object_or_404
from accounts.models import Profile
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from ..serializers import ProfileSerializer


class ProfileApiView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    
    def get_object(self):
        queryset = self.get_queryset()
        return get_object_or_404(queryset, user=self.request.user)
