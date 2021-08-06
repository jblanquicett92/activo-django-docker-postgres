from django.urls import path
from . import views

urlpatterns = [
    path('v1/user/create/', views.CreateUserView.as_view(), name='create'),
    path('v1/user/token/', views.CreateTokenView.as_view(), name='token'),

    path('v1/ltn_lng/', views.UsuarioLatLngView.as_view()),
    
    path('v1/departamentos/', views.Departamentoview.as_view()),
    path('v1/departamentos/<int:id_departamento>',
         views.Departamentoview.as_view()),
    path('v1/turnos/', views.Turnoview.as_view()),
    path('v1/turnos/<int:id_turno>', views.Turnoview.as_view()),
    path('v1/tipos_rol/', views.Tipo_Rolview.as_view()),
    path('v1/tipos_rol/<int:id_tipo_rol>', views.Tipo_Rolview.as_view()),
    path('v1/scopes/', views.Scopeview.as_view()),
    path('v1/scopes/<int:id_scope>', views.Scopeview.as_view()),
    path('v1/estatus/', views.Estatusview.as_view()),
    path('v1/estatus/<int:id_estatus>', views.Estatusview.as_view()),
    path('v1/idiomas/', views.Idiomaview.as_view()),
    path('v1/idiomas/<int:id_idioma>', views.Idiomaview.as_view()),
    path('v1/roles/', views.Rolview.as_view()),
    path('v1/roles/<int:id_rol>', views.Rolview.as_view()),
    path('v1/departamentos_turnos/', views.Departamento_Turnoview.as_view()),
    path('v1/departamentos_turnos/<int:id_departamento_turno>',
         views.Departamento_Turnoview.as_view()),
    path('v1/puestos/', views.Puestoview.as_view()),
    path('v1/puestos/<int:id_puesto>', views.Puestoview.as_view()),
    path('v1/usuarios/', views.Usuarioview.as_view()),
    path('v1/usuarios/<int:id_usuario>', views.Usuarioview.as_view()),
    path('v1/usuarios/<slug:p_nombre>', views.PerfilUsuarioview.as_view()),
    path('v1/historial_turnos/', views.Historial_TurnoView.as_view()),
    path('v1/historial_turnos/<int:id_historial_turno>',
         views.Historial_TurnoView.as_view()),
]
