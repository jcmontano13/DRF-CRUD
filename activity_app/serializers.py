from rest_framework import serializers
from .models import Activity

# serializer for Activity model
# serializer is used to convert the model into JSON format
# serializer is used to validate the data
# translator, validator, and gatekeeper between your database and the outside world.
class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'