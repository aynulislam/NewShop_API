from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import SpProduct,SpCategory,SpSubCategory,SpDivision
from .serializers  import SpProductSerializer,SpCategorySerializer,SpSubCategorySerializer,SpDivisionSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class SpProductAPIView(generics.ListCreateAPIView):
    queryset = SpProduct.objects.all()
    serializer_class = SpProductSerializer

class SpCategoryAPIView(generics.ListCreateAPIView):
    queryset = SpCategory.objects.all()
    serializer_class = SpCategorySerializer

class SpSubCategoryAPIView(generics.ListCreateAPIView):
    queryset = SpSubCategory.objects.all()
    serializer_class = SpSubCategorySerializer

class SpDivisionAPIView(generics.ListCreateAPIView):
    queryset = SpDivision.objects.all()
    serializer_class = SpDivisionSerializer

#Division Api Create

class SpDivisionDetail(APIView):
    """
    Retrieve, update or delete a  instance.
    """
    def get_object(self, pk):
        try:
            return SpDivision.objects.get(pk=pk)
        except SpDivision.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        spdivision = self.get_object(pk)
        serializer = SpDivisionSerializer(spdivision)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        spdivision = self.get_object(pk)
        serializer = SpDivisionSerializer(spdivision, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        spdivision = self.get_object(pk)
        spdivision.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SpDivisionList(APIView):
    """
    List all , or create a new .
    """
    def get(self, request, format=None):
        spdivision = SpDivision.objects.all()
        serializer = SpDivisionSerializer(spdivision, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SpDivisionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Product Api create

class SpProductDetail(APIView):
    """
    Retrieve, update or delete a  instance.
    """
    def get_object(self, pk):
        try:
            return SpProduct.objects.get(pk=pk)
        except SpProduct.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        spproduct = self.get_object(pk)
        serializer = SpProductSerializer(spproduct)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        spproduct = self.get_object(pk)
        serializer = SpProductSerializer(spproduct, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        spproduct = self.get_object(pk)
        spproduct.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SpProductList(APIView):
    """
    List all , or create a new .
    """
    def get(self, request, format=None):
        spproduct = SpProduct.objects.all()
        serializer = SpProductSerializer(spproduct, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SpProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Category Api create

class SpCategoryDetail(APIView):
    """
    Retrieve, update or delete a  instance.
    """
    def get_object(self, pk):
        try:
            return SpCategory.objects.get(pk=pk)
        except SpCategory.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        spcategory = self.get_object(pk)
        serializer = SpCategorySerializer(spcategory)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        spcategory = self.get_object(pk)
        serializer = SpCategorySerializer(spcategory, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        spcategory = self.get_object(pk)
        spcategory.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SpCategoryList(APIView):
    """
    List all , or create a new .
    """
    def get(self, request, format=None):
        spcategory = SpCategory.objects.all()
        serializer = SpCategorySerializer(spcategory, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SpCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#SubCategory Api create

class SpSubCategoryDetail(APIView):
    """
    Retrieve, update or delete a  instance.
    """
    def get_object(self, pk):
        try:
            return SpSubCategory.objects.get(pk=pk)
        except SpSubCategory.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        spsubcategory = self.get_object(pk)
        serializer = SpSubCategorySerializer(spsubcategory)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        spsubcategory = self.get_object(pk)
        serializer = SpSubCategorySerializer(spsubcategory, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        spsubcategory = self.get_object(pk)
        spsubcategory.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SpSubCategoryList(APIView):
    """
    List all , or create a new .
    """
    def get(self, request, format=None):
        spsubcategory = SpSubCategory.objects.all()
        serializer = SpSubCategorySerializer(spsubcategory, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SpSubCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)