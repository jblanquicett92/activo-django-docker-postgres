from ..serializers import ScopeSerializer
from ..models import Scope


class ControllerScope:
    def crearscope(request):
        datosScope = request.data
        scopeNuevo = Scope()
        try:
            scopeNuevo.nombre_scope = datosScope['nombre_scope']
        except Exception:
             return {"estatus":"Error"}
        
        scopeNuevo.save()
        return {"estatus":"Ok", 'scope': scopeNuevo.nombre_scope}

    def listarscope(id_scope=None):
        if id_scope:
            try:
                queryset = Scope.objects.get(id_scope=id_scope)
            except Scope.DoesNotExist:
                return ({'result': 'No se encontró el scope deseado'})
            serializer = ScopeSerializer(queryset)
            return serializer.data
        else:
            queryset = Scope.objects.all()
            serializer = ScopeSerializer(queryset, many=True)
            return serializer.data


