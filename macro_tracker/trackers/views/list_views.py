from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


from ..models.list import List
from ..serializers import ListSerializer, ListReadSerializer
# no authentication ?
class ListsView(APIView):
    # View class for lists/ for viewing all and creating
    serializer_class = ListSerializer # making this alias is not doing us any good
    def get(self, request):
        lists = List.objects.all()
        serializer = ListSerializer(lists, many=True) # naming this serializer is misleading, it is the serialized data being stored in this variable not the serializer itself - also should be pluralized for the index
        return Response({'lists': serializer.data})

    def post(self, request): # not much auth going on in here, we should attach the user making the request to the request data for the new list, so a user cannot make a list for another user if they get creative. also would align with having no nulls
        serializer = ListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ListsDetailView(APIView):
    #  View class for lists/:pk
    serializer_class = ListSerializer # making this alias is not doing us any good ?
    def get(self, request, pk): 
        list = get_object_or_404(List, pk=pk)
        serializer = ListSerializer(list) # not listReadSerializer ? #naming this serializer is misleading, it is the serialized data being stored in this variable not the serializer itself
        return Response({'list': serializer.data})

    def patch(self, request, pk):
        list = get_object_or_404(List, pk=pk)
        serializer = ListSerializer(list, data=request.data)  # why not use the listReadSerializer ? #naming this serializer is misleading, it is the serialized data being stored in this variable not the serializer itself
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# no auth!
    def delete(self, request, pk):
        list = get_object_or_404(List, pk=pk)
        list.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)