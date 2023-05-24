from rest_framework import serializers
from ilonka_cloud.models import UploadedFile


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('file',)
        model = UploadedFile

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)


class FileListSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('file', 'id')
        model = UploadedFile






