from rest_framework import serializers
from .models import File, Words
from pathlib import Path


class FileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = (
            'id',
            'file',
            'name',
            'upload_at',
            'processed',
        )
        read_only_fields = (
            'id',
            'name',
            'upload_at',
            'processed',
        )

    def validate(self, data):
        file = self.initial_data.get('file')
        suffix = Path(file.name).suffix
        if suffix != '.txt':
            raise serializers.ValidationError({
                'file': 'Используйте расширение .txt'
            })
        return data


class FileListSerializer(serializers.ModelSerializer):
    quantity = serializers.SerializerMethodField()

    class Meta:
        model = File
        fields = (
            'id',
            'name',
            'upload_at',
            'quantity',
            'processed',
        )

    def get_quantity(self, file):
        qs = file.words.values('quantity')
        return list(qs)[0]['quantity']


class WordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Words
        fields = ('quantity', 'words_list', )


class FileRetrieveSerializer(serializers.ModelSerializer):
    words = WordsSerializer(many=True, read_only=True)

    class Meta:
        model = File
        fields = (
            'name',
            'upload_at',
            'words',
            'processed',
        )
