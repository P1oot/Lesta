from rest_framework import serializers
from .models import File
from pathlib import Path


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = (
            'id', 'file', 'name', 'upload_at', 'processed', 'words_list'
        )
        read_only_fields = (
            'id', 'name', 'upload_at', 'processed', 'words_list'
        )

    def validate(self, data):
        file = self.initial_data.get('file')
        suffix = Path(file.name).suffix
        if suffix != '.txt':
            raise serializers.ValidationError({
                'file': 'Используйте расширение .txt'
            })
        return data
