from ..serializers import EstatusSerializer
from ..models import EstatusUsuario


class ControllerEstatus:
    def crearestatus(request):
        datosEstatus = request.data
        estatusNuevo = EstatusUsuario()
        try:
            estatusNuevo.activo = datosEstatus['activo']
            estatusNuevo.nombre=datosEstatus['nombre']
        except Exception:
             return {"estatus":"Error"}

        estatusNuevo.save()
        return {"estatus":"Ok", 'scope': estatusNuevo.activo}

    def listarestatus(id_estatus=None):
        if id_estatus:
            try:
                queryset = EstatusUsuario.objects.get(id_estatus=id_estatus)
            except EstatusUsuario.DoesNotExist:
                return ({'result': 'No se encontró el estatus deseado'})
            serializer = EstatusSerializer(queryset)
            return serializer.data
        else:
            queryset = EstatusUsuario.objects.all()
            serializer = EstatusSerializer(queryset, many=True)
            return serializer.data


