from rest_framework import viewsets
from escola.models import Aluno, Curso
from escola.serializer import AlunoSerializer, CursoSerializer

class AlunoViewSet(viewsets.ModelViewSet):
    """"Um viewset para visualizar e editar alunos"""
    serializer_class = AlunoSerializer
    queryset = Aluno.objects.all()

class CursoViewSet(viewsets.ModelViewSet):
    """"Um viewset para visualizar e editar cursos"""
    serializer_class = CursoSerializer
    queryset = Curso.objects.all()


