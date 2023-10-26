from rest_framework import serializers

from .models import (
    Empresa,
    Registro
)


class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = "__all__"


class RegistroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registro
        fields = "__all__"
