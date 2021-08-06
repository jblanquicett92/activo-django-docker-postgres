from ..serializers import PuestoSerializer  
from ..models import Puesto, Departamento_Turno


class ControllerPuesto:
    def crearpuesto(request):
        datosPuesto = request.data
        try:
            departamento_turno = Departamento_Turno.objects.get(id_departamento_turno=datosPuesto['departamento_turno'])
            puestoNuevo = Puesto.objects.create(
                nombre_puesto = datosPuesto['nombre_puesto'],
                departamento_turno = departamento_turno,
            )
                
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'nuevo_puesto': puestoNuevo.nombre_puesto}
       
    def listarpuesto(id_puesto=None):
        if id_puesto:
            try:
                queryset = Puesto.objects.get(id_puesto=id_puesto)
            except Puesto.DoesNotExist:
                return ({'result': 'No se encontró el puesto deseado'})
            serializer = PuestoSerializer(queryset)
            return serializer.data
        else:
            queryset = Puesto.objects.all()
            serializer = PuestoSerializer(queryset, many=True)
            return serializer.data
