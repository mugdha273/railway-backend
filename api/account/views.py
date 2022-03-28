from django.shortcuts import render
from account.models import Account
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from account.serializers import AccountSerializer
from rest_framework.response import Response
from rest_framework import status


# Create your views here.


class SignUpView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = AccountSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors)

        user_data = serializer.validated_data
        
        user = Account.objects.create_user(**user_data)
        return Response({"status": "User created successfully"}, status=status.HTTP_201_CREATED)