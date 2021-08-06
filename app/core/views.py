from rest_framework import generics, serializers
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from .controller.ControllerHistTurno import ControllerHistTurno
from .controller.ControllerPuesto import ControllerPuesto
from .controller.ControllerIdioma import ControllerIdioma
from .controller.ControllerDept import ControllerDept
from .controller.ControllerUsuario import ControllerUsuario
from .controller.ControllerTurno import ControllerTurno
from .controller.ControllerTipoRol import ControllerTipoRol
from .controller.ControllerScope import ControllerScope
from .controller.ControllerEstatus import ControllerEstatus
from .controller.ControllerRol import ControllerRol
from .controller.ControllerLogin import ControllerLogin
from .controller.ControllerDeptTurno import ControllerDeptTurno
from .assets.DistanciaEntrePuntos import DistanciaEntrePuntos

from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import Departamento_TurnoSerializer, EstatusSerializer, IdiomaSerializer, PuestoSerializer, RolSerializer, ScopeSerializer, Tipo_RolSerializer, TurnoSerializer, UserSerializer, AuthTokenSerializer, DepartamentoSerializer, UsuarioSerializer
from .serializers import Usuario_Lat_Lng_Serializer, TurnoSerializer


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system"""
    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for the user"""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UsuarioLatLngView(GenericAPIView):

    serializer_class = Usuario_Lat_Lng_Serializer

    def post(self, request, *args, **kwargs):

        lat_us = float(request.data['lat_usuario'])
        lon_us = float(request.data['lon_usuario'])
        lat_em = float(request.data['lat_empresa'])
        lon_em = float(request.data['lon_empresa'])
        print(request.data)
        mts = round (DistanciaEntrePuntos.distancia_km(
            lat1=lat_us, lon1=lon_us, lat2=lat_em, lon2=lon_em), 2)
        acceso = True if mts<50 else False
        return Response({'distancia_usuario_planta': f'{mts} metros', 'acceso':acceso})


class Departamentoview(APIView):
    serializer_class = DepartamentoSerializer

    def post(self, request):
        respuesta = ControllerDept.creardepartamento(request)
        return Response(respuesta)

    def get(self, request, id_departamento=None):
        respuesta = ControllerDept.listardepartamento(id_departamento)
        return Response(respuesta)


class Turnoview(APIView):
    serializer_class = TurnoSerializer

    def post(self, request):
        respuesta = ControllerTurno.crearturno(request)
        return Response(respuesta)

    def get(self, request, id_turno=None):
        respuesta = ControllerTurno.listarturno(id_turno)
        return Response(respuesta)


class Tipo_Rolview(APIView):
    serializer_class = Tipo_RolSerializer

    def post(self, request):
        respuesta = ControllerTipoRol.creartipo_rol(request)
        return Response(respuesta)

    def get(self, request, id_tipo_rol=None):
        respuesta = ControllerTipoRol.listartipo_rol(id_tipo_rol)
        return Response(respuesta)


class Scopeview(APIView):
    serializer_class = ScopeSerializer

    def post(self, request):
        respuesta = ControllerScope.crearscope(request)
        return Response(respuesta)

    def get(self, request, id_scope=None):
        respuesta = ControllerScope.listarscope(id_scope)
        return Response(respuesta)


class Estatusview(APIView):
    serializer_class = EstatusSerializer

    def post(self, request):
        respuesta = ControllerEstatus.crearestatus(request)
        return Response(respuesta)

    def get(self, request, id_estatus=None):
        respuesta = ControllerEstatus.listarestatus(id_estatus)
        return Response(respuesta)


class Idiomaview(APIView):
    serializer_class = IdiomaSerializer

    def post(self, request):
        respuesta = ControllerIdioma.crearidioma(request)
        return Response(respuesta)

    def get(self, request, id_idioma=None):
        respuesta = ControllerIdioma.listariridioma(id_idioma)
        return Response(respuesta)


class Rolview(APIView):
    serializer_class = RolSerializer

    def post(self, request):
        respuesta = ControllerRol.crearrol(request)
        return Response(respuesta)

    def get(self, request, id_rol=None):
        respuesta = ControllerRol.listarrol(id_rol)
        return Response(respuesta)


class Departamento_Turnoview(APIView):
    serializer_class = Departamento_TurnoSerializer

    def post(self, request):
        respuesta = ControllerDeptTurno.creardepartamento_turno(request)
        return Response(respuesta)

    def get(self, request, id_departamento_turno=None):
        respuesta = ControllerDeptTurno.listardepartamento_turno(
            id_departamento_turno)
        return Response(respuesta)


class Puestoview(APIView):
    serializer_class = PuestoSerializer

    def post(self, request):
        respuesta = ControllerPuesto.crearpuesto(request)
        return Response(respuesta)

    def get(self, request, id_puesto=None):
        respuesta = ControllerPuesto.listarpuesto(id_puesto)
        return Response(respuesta)


class Usuarioview(APIView):
    serializer_class = UsuarioSerializer

    def post(self, request):
        respuesta = ControllerUsuario.crearUsuario(request)
        return Response(respuesta)

    def get(self, request, id_usuario=None):
        respuesta = ControllerUsuario.listarUsuario(id_usuario)
        return Response(respuesta)


class PerfilUsuarioview(APIView):
    def get(self, request, p_nombre=None):
        respuesta = ControllerUsuario.verPerfil(p_nombre)
        return Response(respuesta)


class Historial_TurnoView(APIView):
    def post(self, request):
        respuesta = ControllerHistTurno.crearhistorial_turno(request)
        return Response(respuesta)

    def get(self, request, id_historial_turno=None):
        respuesta = ControllerHistTurno.listarhistorialturno(
            id_historial_turno)
        return Response(respuesta)


class LoginView(APIView):
    def post(self, request):
        respuesta = ControllerLogin.login(request)
        return Response(respuesta)
