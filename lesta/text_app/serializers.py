from rest_framework import serializers
from .models import File, Words


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ('file', 'processed',)
        read_only_fields = ('processed',)


class WordsSerializer(serializers.ModelSerializer):
    idf = serializers.SerializerMethodField()

    class Meta:
        model = Words
        fields = ('word', 'quantity', 'tf')

    def get_idf(self, obj):
        pass
