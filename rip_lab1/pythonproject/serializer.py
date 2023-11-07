from rest_framework import serializers

from .models import *

class AudiencesSerializer(serializers.ModelSerializer):

    class Meta:

        model = Audiences

        fields = "__all__"





class Booking_requestsSerializer(serializers.ModelSerializer):

    pioneer = AudiencesSerializer(read_only=True, many=True)



    class Meta:

        model = Booking_requests

        fields = "__all__"

