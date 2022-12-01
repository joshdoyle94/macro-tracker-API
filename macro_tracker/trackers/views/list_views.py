from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


from ..models.list import List
from ..serializers import ListSerializer, ListReadSerializer

class ListsView(APIView):
    # View class for lists/ for viewing all and creating
    serializer_class = ListSerializer
    def get(self, request):
        lists = List.objects.all()
        serializer = ListSerializer(lists, many=True)
        return Response({'lists': serializer.data})

    def post(self, request):
        serializer = ListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ListsDetailView(APIView):
    #  View class for lists/:pk
    serializer_class = ListSerializer
    def get(self, request, pk):
        list = get_object_or_404(List, pk=pk)
        serializer = ListSerializer(list)
        return Response({'list': serializer.data})

    def patch(self, request, pk):
        list = get_object_or_404(List, pk=pk)
        serializer = ListSerializer(list, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        list = get_object_or_404(List, pk=pk)
        list.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)