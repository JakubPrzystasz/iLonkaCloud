from django.shortcuts import render
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from ilonka_cloud.models import UploadedFile
from ilonka_cloud.serializers import FileSerializer, FileListSerializer


# Create your views here.
class UploadView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = FileSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save()

            return Response(status=201)

        return Response(status=400)


class FileListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        queryset = UploadedFile.objects.filter(user=request.user)
        serializer = FileListSerializer(queryset, many=True)

        return Response(serializer.data, status=200)


class IsUserOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj == request.user


class FileDeleteView(APIView):
    permission_classes = [IsUserOwner]

    def delete(self, request):
        pass

