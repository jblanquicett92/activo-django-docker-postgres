from ..serializers import Departamento_TurnoSerializer  
from ..models import Departamento_Turno, Departamento, Turno


class ControllerDeptTurno:
    def creardepartamento_turno(request):
        datosDepartamentoTurno = request.data
        try:
            departamento = Departamento.objects.get(id_departamento=datosDepartamentoTurno['departamento'])
            turno = Turno.objects.get(id_turno=datosDepartamentoTurno['turno'])
            departamentoTurnoNuevo = Departamento_Turno.objects.create(
                departamento = departamento,
                turno = turno,
            )
                
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'nuevo_departamento_turno': departamentoTurnoNuevo.id_departamento_turno}
       
    def listardepartamento_turno(id_departamento_turno=None):
        if id_departamento_turno:
            try:
                queryset = Departamento_Turno.objects.get(id_departamento_turno=id_departamento_turno)
            except Departamento_Turno.DoesNotExist:
                return ({'result': 'No se encontró la relación departamento turno deseada'})
            serializer = Departamento_TurnoSerializer(queryset)
            return serializer.data
        else:
            queryset = Departamento_Turno.objects.all()
            serializer = Departamento_TurnoSerializer(queryset, many=True)
            return serializer.data
