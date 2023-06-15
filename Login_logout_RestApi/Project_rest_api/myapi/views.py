# Firt way to create rest Api

# from django.shortcuts import render
# from .models import Employee
# from .serializers import EmployeeSerializer
# from rest_framework.renderers import JSONRenderer
# from django.http import HttpResponse,JsonResponse
# from rest_framework.parsers import JSONParser
# import io
# from django.views.decorators.csrf import csrf_exempt
# # Create your views here.


# # def Employee_data(request, pk):
# #     emp = Employee.objects.get(id= pk)
# #     serializer = EmployeeSerializer(emp)
# #     json_data = JSONRenderer().render(serializer.data)
# #     return HttpResponse(json_data, content_type='application/json')







# # insert data   
#def Employee_data_create(request):    
#     if request.method == 'POST':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythonDictData = JSONParser().parse(stream)
#         dataSerialize = EmployeeSerializer(data = pythonDictData)
#         if dataSerialize.is_valid():
#             dataSerialize.save()
#             msg = {'message':' Your Form Submited !'}
#             json_data = JSONRenderer().render(msg)
#             return HttpResponse(json_data, content_type='application/json')
#         else:
#             json_data = JSONRenderer().render(dataSerialize.errors)
#             return HttpResponse(json_data, content_type='application/json')
#def Employee_data_update(request):
#     if request.method == 'PUT':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythonDictData = JSONParser().parse(stream)
#         id = pythonDictData.get('id')
#         emp = Employee.objects.get(id=id)
#         dataSerialize = EmployeeSerializer(emp, data = pythonDictData, partial=True)
#         if dataSerialize.is_valid():
#             dataSerialize.save()
#             msg = {'message':' Your Form updated !'}
#             json_data = JSONRenderer().render(msg)
#             return HttpResponse(json_data, content_type='application/json')
#def Employee_data_delete(request):
#     if request.method == 'DELETE':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythonDictData = JSONParser().parse(stream)
#         id = pythonDictData.get('id')
#         emp = Employee.objects.get(id=id)
#         emp.delete()
#         msg = {'message':' Your Form deleted !'}
#         json_data = JSONRenderer().render(msg)
#         return HttpResponse(json_data, content_type='application/json')


# second way Create rest Api  


# from .models import Employee
# from .serializers import EmployeeSerializer      
# from rest_framework.decorators import api_view
# from rest_framework.response import Response

# @api_view(['GET', 'POST', 'PUT', 'DELETE'])
# def Employee_data_insert(request):
#     if request.method == 'GET':
#         id = request.query_params.get('id')
#         if id is not None:
#             try:
#                 emp = Employee.objects.get(id=id)
#                 serializer = EmployeeSerializer(emp)
#                 return Response(serializer.data)
#             except Employee.DoesNotExist:
#                 return Response({'message': 'Employee not found'}, status=404)

#         employees = Employee.objects.all()
#         serializer = EmployeeSerializer(employees, many=True)
#         return Response(serializer.data)
    
#     if request.method == 'POST':
#         serializer = EmployeeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'message': 'Your Form Submitted!'})
#         return Response(serializer.errors, status=400)
    
#     if request.method == 'PUT':
#         id = request.data.get('id')
#         try:
#             emp = Employee.objects.get(id=id)
#             serializer = EmployeeSerializer(emp, data=request.data, partial=True)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response({'message': 'Your Form updated!'})
#             return Response(serializer.errors, status=400)
#         except Employee.DoesNotExist:
#             return Response({'message': 'Employee not found'}, status=404)
    
#     if request.method == 'DELETE':
#         id = request.data.get('id')
#         try:
#             emp = Employee.objects.get(id=id)
#             emp.delete()
#             return Response({'message': 'Your Form deleted!'})
#         except Employee.DoesNotExist:
#             return Response({'message': 'Employee not found'}, status=404)



# # class view funtion 

# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .models import Employee
# from .serializers import EmployeeSerializer
# from rest_framework.authentication import BaseAuthentication
# from rest_framework.permissions import IsAuthenticated




# class EmployeeDataInsertAPIView(APIView):
#     def get(self, request, format=None):
#         id = request.query_params.get('id')
#         if id is not None:
#             try:
#                 emp = Employee.objects.get(id=id)
#                 serializer = EmployeeSerializer(emp)
#                 return Response(serializer.data)
#             except Employee.DoesNotExist:
#                 return Response({'message': 'Employee not found'}, status=status.HTTP_404_NOT_FOUND)

#         employees = Employee.objects.all()
#         serializer = EmployeeSerializer(employees, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = EmployeeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'message': 'Your Form Submitted!'}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def put(self, request, format=None):
#         id = request.data.get('id')
#         try:
#             emp = Employee.objects.get(id=id)
#             serializer = EmployeeSerializer(emp, data=request.data, partial=True)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response({'message': 'Your Form updated!'})
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         except Employee.DoesNotExist:
#             return Response({'message': 'Employee not found'}, status=status.HTTP_404_NOT_FOUND)

#     def delete(self, request, format=None):
#         id = request.data.get('id')
#         try:
#             emp = Employee.objects.get(id=id)
#             emp.delete()
#             return Response({'message': 'Your Form deleted!'})
#         except Employee.DoesNotExist:
#             return Response({'message': 'Employee not found'}, status=status.HTTP_404_NOT_FOUND)
    


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
    
