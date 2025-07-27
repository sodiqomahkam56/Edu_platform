from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import Homework
from core.serializers import HomeworkSerializer, HomeworkDetailSerializer


class HomeworkViewSet(viewsets.ModelViewSet):
    queryset = Homework.objects.all()
    serializer_class = HomeworkSerializer

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(user=self.request.user)
        else:
            serializer.save()

class HomeworkListView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        homeworks = Homework.objects.all()
        serializer = HomeworkSerializer(homeworks, many=True)
        return Response(serializer.data)

class HomeworkDetailView(APIView):
    def get(self, request, pk):
        try:
            homework = Homework.objects.get(pk=pk)
        except Homework.DoesNotExist:
            return Response({"detail": "Not found."}, status=404)

        serializer = HomeworkDetailSerializer(homework)
        return Response(serializer.data)

class HomeworkUpdateView(APIView):
    def put(self, request, pk):
        homework = Homework.objects.get(pk=pk)
        serializer = HomeworkSerializer(homework, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class HomeworkDeleteView(APIView):
    def delete(self, request, pk):
        homework = Homework.objects.get(pk=pk)
        homework.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


