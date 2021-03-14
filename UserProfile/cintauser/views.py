from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer
from .models import CintaUser
from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie


@method_decorator(cache_page(60*60*2))
@api_view(['GET', 'POST', 'DELETE'])
def user_list(request):
    if request.method == 'GET':
        users = CintaUser.objects.all()
        name = request.GET.get('name', None)
        if name is not None:
            users = users.filter(name__icontains=name)

        users_serializer = UserSerializer(users, many=True)
        return JsonResponse(users_serializer.data, safe=False)
        # 'safe=False' for objects serialization
    # GET list of tutorials, POST a new tutorial, DELETE all tutorials
    elif request.method == 'POST':
        user_data = request.data
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse(user_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@method_decorator(cache_page(60*60*2))
@method_decorator(vary_on_cookie)
@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, pk):
    # find tutorial by pk (id)
    try:
        tutorial = CintaUser.objects.get(pk=pk)
    except CintaUser.DoesNotExist:
        return JsonResponse({'message': 'The User does not exist'}, status=status.HTTP_404_NOT_FOUND)

        # GET / PUT / DELETE tutorial
    if request.method == 'GET':
        user_serializer = UserSerializer(user_list)
        return JsonResponse(user_serializer.data)
    elif request.method == 'PUT':
        user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(tutorial, data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse(user_serializer.data)
        return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)