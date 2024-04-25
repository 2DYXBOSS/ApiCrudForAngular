from django.http import Http404
from django.shortcuts import render
from monapp.models import Monmodel
from monapp.serializers import Monserialiser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class Apilist(APIView):
  
    def get(self , request):
        recuperer = Monmodel.objects.all()
        seria = Monserialiser(recuperer , many = True)
        return Response(seria.data)
    
    def post(self , request):
        ajouter= Monserialiser(data=request.data)

        if ajouter.is_valid():
            ajouter.save()
            return Response(ajouter.data)
        return Response(ajouter.data)
    

class Apiunique(APIView):
    def get_object(self, pk):
        try:
            return Monmodel.objects.get(pk=pk)
        except Monmodel.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        book = self.get_object(pk)
        serializer = Monserialiser(book)
        return Response(serializer.data)
    
    def put(self , request, pk):
        book = self.get_object(pk)
        serializer = Monserialiser(book,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.data)
    
    def delete(self, request, pk):
        book = self.get_object(pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)