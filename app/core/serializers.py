from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers

from .models import Departamento, EstatusUsuario, Historial_Turno, Idioma, Puesto, Scope, Tipo_Rol, Rol
from .models import Departamento_Turno, Turno, Puesto, Usuario


class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = '__all__'


class TurnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turno
        fields = '__all__'


class Tipo_RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo_Rol
        fields = '__all__'


class ScopeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scope
        fields = '__all__'


class EstatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstatusUsuario
        fields = '__all__'


class IdiomaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Idioma
        fields = '__all__'


class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = '__all__'
        depth = 1


class Departamento_TurnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento_Turno
        fields = '__all__'
        depth = 1


class PuestoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Puesto
        fields = '__all__'
        depth = 2


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
        depth = 2


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('email', 'password', 'username')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)


class AuthTokenSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, attrs):
        """Validate and authenticate the user"""
        email = attrs.get('email')
        password = attrs.get('password')

        user = authenticate(
            request=self.context.get('request'),
            username=email,
            password=password
        )
        if not user:
            msg = _('Unable to authenticate with provided credentials')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs


class Historial_TurnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Historial_Turno
        fields = '__all__'
        depth = 4


class Usuario_Lat_Lng_Serializer(serializers.Serializer):

    lat = serializers.CharField(max_length=40, allow_blank=False)
    lng = serializers.CharField(max_length=40, allow_blank=False)

    class Meta:
        fields = ('Lat', 'lng')
