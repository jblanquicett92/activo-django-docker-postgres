from ..serializers import TurnoSerializer
from ..models import Turno


class ControllerTurno:
    def crearturno(request):
        datosTurno = request.data
        TurnoNuevo = Turno()
        try:
            TurnoNuevo.nombre_turno = datosTurno['nombre_turno']
            TurnoNuevo.hora_inicio = datosTurno['hora_inicio']
            TurnoNuevo.hora_fin = datosTurno['hora_fin']
        except Exception:
             return {"estatus":"Error"}
        
        TurnoNuevo.save()
        return {"estatus":"Ok", 'nuevo_turno': TurnoNuevo.nombre_turno}

    def listarturno(id_turno=None):
        if id_turno:
            try:
                queryset = Turno.objects.get(id_turno=id_turno)
            except Turno.DoesNotExist:
                return ({'result': 'No se encontró el turno deseado'})
            serializer = TurnoSerializer(queryset)
            return serializer.data
        else:
            queryset = Turno.objects.all()
            serializer = TurnoSerializer(queryset, many=True)
            return serializer.data


