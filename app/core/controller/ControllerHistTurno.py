from ..serializers import Historial_TurnoSerializer  
from ..models import Historial_Turno, Usuario, Puesto


class ControllerHistTurno:
    def crearhistorial_turno(request):
        datosHistorialTurno = request.data
        try:
            usuario = Usuario.objects.get(id_usuario=datosHistorialTurno['usuario'])
            puesto = Puesto.objects.get(id_puesto=datosHistorialTurno['puesto'] )
            historialTurnoNuevo = Historial_Turno.objects.create(
                milisegundos = datosHistorialTurno['milisegundos'],
                fecha = datosHistorialTurno['fecha'],
                puesto = puesto,
                usuario = usuario,
            )
                
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'nuevo_historial_turno': historialTurnoNuevo.id_historial_turno}
       
    def listarhistorialturno(id_historial_turno=None):
        if id_historial_turno:
            try:
                queryset = Historial_Turno.objects.get(id_historial_turno=id_historial_turno)
            except Historial_Turno.DoesNotExist:
                return ({'result': 'No se encontró el historial de turno deseado'})
            serializer = Historial_TurnoSerializer(queryset)
            return serializer.data
        else:
            queryset = Historial_Turno.objects.all()
            serializer = Historial_TurnoSerializer(queryset, many=True)
            return serializer.data
