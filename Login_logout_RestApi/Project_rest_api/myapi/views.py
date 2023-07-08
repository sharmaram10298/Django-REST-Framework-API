# viewsetApi method

# from django.shortcuts import render
# from rest_framework.response import Response
from .models import Employee
from .serializers import EmployeeSerializer
# from rest_framework import status
from rest_framework import viewsets
# from rest_framework.authentication import BasicAuthentication # BasicAuthentication
from rest_framework.authentication import SessionAuthentication
# from rest_framework.permissions import IsAuthenticated, AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly, DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly

from .custompermission import EmployeePermission


class EmployeeModelViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    # authentication_classes = [BasicAuthentication] # BasicAuthentication
    authentication_classes = [SessionAuthentication] # SessionAuthentication
    # permission_classes = [IsAuthenticated]
    # permission_classes = [AllowAny]
    # permission_classes = [IsAdminUser]
    # permission_classes = [IsAuthenticatedOrReadOnly]
    # permission_classes = [DjangoModelPermissions]
    # permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    permission_classes = [EmployeePermission]
    
