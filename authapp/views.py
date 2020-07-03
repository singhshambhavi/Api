from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.shortcuts import render
from django.http import JsonResponse
from .models import CustomUser

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def restricted(request, *args, **kwargs):
    current_user = request.user
    user_detail= CustomUser.objects.filter(email=current_user)
    detail_dict=[]
    for i in user_detail:
        detail_list=dict()
        detail_list["username"]=i.username
        detail_list["email"]=i.email
        detail_list["dob"]=i.dob
        detail_dict.append(detail_list)
    return Response(detail_dict)

@api_view(['GET'])
def authenticate(request,*args, **kwargs):
    if (request.user.is_authenticated == True): 
        message='Authentication Sucessfull!'
        return Response(data=message, status=status.HTTP_200_OK)
    else:
        return Response(data="Authentication Not Sucessfull!", status=status.HTTP_200_OK)   


@api_view(['GET'])
def CurrentUser(request):
    if request.user.is_authenticated == False:
        current_user = request.user
        print (current_user.id)
        user_detail= CustomUser.objects.filter(used_id=current_user)
        return JsonResponse(user_detail.username, user_detail.email, user_detail.dob)
    else:
        return Response(data="Authenticated Users Only", status=status.HTTP_200_OK)

@api_view(['GET'])
def details(request):
    user_obj= CustomUser.objects.all()
    detail_dict=[]
    for i in user_obj:
        detail_list=dict()
        detail_list["username"]=i.username
        detail_list["email"]=i.email
        detail_list["dob"]=i.dob
        detail_dict.append(detail_list)
    return Response(detail_dict)