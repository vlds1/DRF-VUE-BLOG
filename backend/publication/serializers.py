from rest_framework import serializers
from .models import CategoryModel, PublicationModel

# serializers.ModelSerializer - serializer that works with models
class PublSerializer(serializers.ModelSerializer):
    # title = serializers.CharField(max_length=100)
    # img = serializers.ImageField()
    # content = serializers.CharField()
    # created_at = serializers.DateTimeField()
    # updated_at = serializers.DateTimeField()
    # is_published = serializers.BooleanField(default=True)
    
    
    class Meta:
        model = PublicationModel
        fields = '__all__'
