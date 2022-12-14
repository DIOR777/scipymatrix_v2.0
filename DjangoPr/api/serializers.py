from rest_framework import serializers


class ArrayDiagonaleSerializers(serializers.Serializer):
    massiv = serializers.ListField(child=serializers.CharField())
    diagonal = serializers.CharField()
