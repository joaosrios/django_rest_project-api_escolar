from rest_framework import viewsets, generics
from escola.models import Aluno, Curso, Matricula
from escola.serializer import AlunoSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculasAlunoSerializer

class AlunoViewSet(viewsets.ModelViewSet):
    """"Um viewset para visualizar e editar alunos"""
    serializer_class = AlunoSerializer
    queryset = Aluno.objects.all()

class CursoViewSet(viewsets.ModelViewSet):
    """"Um viewset para visualizar e editar cursos"""
    serializer_class = CursoSerializer
    queryset = Curso.objects.all()

class MatriculaViewSet(viewsets.ModelViewSet):
    """Visualizando todas as matriculas"""
    serializer_class = MatriculaSerializer
    queryset = Matricula.objects.all()

class ListaMatriculasAluno(generics.ListAPIView):
    """Listando as matriculas do aluno"""
    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculasAlunoSerializer
