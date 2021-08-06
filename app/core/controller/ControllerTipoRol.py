from ..serializers import Tipo_RolSerializer
from ..models import Tipo_Rol


class ControllerTipoRol:
    def creartipo_rol(request):
        datosTipoRol = request.data
        tipoRolNuevo = Tipo_Rol()
        try:
            tipoRolNuevo.nombre_tipo_rol = datosTipoRol['nombre_tipo_rol']
        except Exception:
             return {"estatus":"Error"}
        
        tipoRolNuevo.save()
        return {"estatus":"Ok", 'tipo_rol': tipoRolNuevo.nombre_tipo_rol}

    def listartipo_rol(id_tipo_rol=None):
        if id_tipo_rol:
            try:
                queryset = Tipo_Rol.objects.get(id_tipo_rol=id_tipo_rol)
            except Tipo_Rol.DoesNotExist:
                return ({'result': 'No se encontró el tipo de rol deseado'})
            serializer = Tipo_RolSerializer(queryset)
            return serializer.data
        else:
            queryset = Tipo_Rol.objects.all()
            serializer = Tipo_RolSerializer(queryset, many=True)
            return serializer.data


