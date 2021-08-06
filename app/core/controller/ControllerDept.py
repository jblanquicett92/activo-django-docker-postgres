from ..serializers import DepartamentoSerializer
from ..models import Departamento


class ControllerDept:
    serializer_class = DepartamentoSerializer
        
    def creardepartamento(request):
        datosDepartamento = request.data
        departamentoNuevo = Departamento()
        try:
            departamentoNuevo.nombre_departamento = datosDepartamento['nombre_departamento']
        except Exception:
             return {"estatus":"Error"}
        
        departamentoNuevo.save()
        return {"estatus":"Ok", 'nuevo_departamento': departamentoNuevo.nombre_departamento}

    def listardepartamento(id_departamento=None):
        if id_departamento:
            try:
                queryset = Departamento.objects.get(id_departamento=id_departamento)
            except Departamento.DoesNotExist:
                return ({'result': 'No se encontró el departamento deseado'})
            serializer = DepartamentoSerializer(queryset)
            return serializer.data
        else:
            queryset = Departamento.objects.all()
            serializer = DepartamentoSerializer(queryset, many=True)
            return serializer.data


