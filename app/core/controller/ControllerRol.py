from ..serializers import RolSerializer
from ..models import Rol, Tipo_Rol, Scope


class ControllerRol:
    def crearrol(request):
        datosRol = request.data
        try:
            tipo_rol = Tipo_Rol.objects.get(id_tipo_rol=datosRol['tipo_rol'])
            scope = Scope.objects.get(id_scope=datosRol['scope'])
            rolNuevo = Rol.objects.create(
                nombre=datosRol['nombre'],
                tipo_rol = tipo_rol,
                scope = scope,
            )
                
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'nuevo_rol': rolNuevo.id_rol}
       
    def listarrol(id_rol=None):
        if id_rol:
            try:
                queryset = Rol.objects.get(id_rol=id_rol)
            except Rol.DoesNotExist:
                return ({'result': 'No se encontró el rol deseado'})
            serializer = RolSerializer(queryset)
            return serializer.data
        else:
            queryset = Rol.objects.all()
            serializer = RolSerializer(queryset, many=True)
            return serializer.data

