from django.contrib import admin
from django.urls import path, include
from escola.views import AlunoViewSet, CursoViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('alunos', AlunoViewSet, basename='Alunos')
router.register('cursos', CursoViewSet, basename='Cursos')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls)),
]
