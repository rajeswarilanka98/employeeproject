from datetime import datetime
from urllib import request

from django.shortcuts import render
# Create your views here.
from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.templatetags.rest_framework import data
from rest_framework.views import APIView

from .models import Employee
# from serializer import EmployeeSerializer
from .serializers import EmployeeSerializer, loginSerializer
import logging
logger = logging.getLogger(__name__)


class EmployeeView(APIView):
    def post(self, request):
        data={}
        service_start_time = datetime.now()
        logger.info('createapi statrted')
        logger.info('createapi statrted time: '+str(service_start_time))
        logger.info('createapi request object: ' + str(request.data))
        serializer = EmployeeSerializer( data=request.data)
        if serializer.is_valid():
            serializer.save()
            data["responseCode"] = status.HTTP_200_OK
            data["typeCode"] = status.HTTP_201_CREATED
            data['message'] = "success"
            data['Data'] = serializer.data
            service_end_time = datetime.now()
            logger.info('createapi ends')
            logger.info('createapi ends time:'+str(service_end_time))
            logger.info('createapi response :' + str(data))
            return Response(data=data)
        else:
            data["responseCode"] = status.HTTP_400_BAD_REQUEST
            return Response(data=data)

class EmployeeGetView(APIView):
    def get(self, request):
        data={}
        service_start_time = datetime.now()
        logger.info('getapi statrted')
        logger.info('getapi statrted time: ' + str(service_start_time))
        logger.info('getapi request object: ' + str(request.data))
        employee= Employee.objects.all()
        serializer =EmployeeSerializer(employee,many=True)
        data["responseCode"] = status.HTTP_200_OK
        data["typeCode"] = status.HTTP_201_CREATED
        data['message'] = "success"
        data['Data'] = serializer.data
        service_end_time = datetime.now()
        logger.info('getapi ends')
        logger.info('getapi ends time:' + str(service_end_time))
        logger.info('getapi response :' + str(data))
        return Response(data=data)

class EmployeePutView(APIView):
    def put(self, request, pk):
        data={}
        service_start_time = datetime.now()
        logger.info('updateapi statrted')
        logger.info('updateapi statrted time: ' + str(service_start_time))
        logger.info('updateapi request object: ' + str(request.data))
        employee = Employee.objects.get(empID=pk)
        serializer = EmployeeSerializer(employee,data=request.data)
        if serializer.is_valid():
           serializer.save()
           data["responseCode"] = status.HTTP_200_OK
           data["typeCode"] = status.HTTP_201_CREATED
           data['message'] = "success"
           data['Data'] = serializer.data
           service_end_time = datetime.now()
           logger.info('updateapi ends')
           logger.info('updateapi ends time:' + str(service_end_time))
           logger.info('updateapi response :' + str(data))
        return Response(data=data)

class EmployeeDeleteView(APIView):
    def delete(self,request):
        data={}
        service_start_time = datetime.now()
        logger.info('deleteapi statrted')
        logger.info('deleteapi statrted time: ' + str(service_start_time))
        logger.info('deleteapi request object: ' + str(request.data))
        empID=request.get('empID')
        employee = Employee.objects.get(empID=empID)
        if employee:
           print(employee)
           employee.delete()
           data["responseCode"] = status.HTTP_200_OK
           data['message'] = "deleted data successfully"
           service_end_time = datetime.now()
           logger.info('deleteapi ends')
           logger.info('deleteapi ends time:' + str(service_end_time))
           logger.info('deleteapi response :' + str(data))
           return Response(data=data)


class loginApi(APIView):
    def post(self, request):
        data={}
        service_start_time = datetime.now()
        logger.info('loginapi statrted')
        logger.info('loginapi statrted time: ' + str(service_start_time))
        logger.info('loginapi request object: ' + str(request.data))
        empdata=Employee.objects.filter(empEmail=request.data['empEmail'],password=request.data['password'])
        print(empdata)
        serializer = EmployeeSerializer(empdata)
        print(serializer)
        data["responseCode"] = status.HTTP_200_OK
        data["typeCode"] = status.HTTP_201_CREATED
        data['message'] = "success"
        data['Data'] = serializer.data
        service_end_time = datetime.now()
        logger.info('loginapi ends')
        logger.info('loginapi ends time:' + str(service_end_time))
        logger.info('loginapi response :' + str(data))
        # else:
        #     data["responseCode"] = status.HTTP_400_BAD_REQUEST
        #     data["typeCode"] = status.HTTP_404_NOT_FOUND
        #     data["details"] = 'Invalid credentials, try again'
        #     return Response(data=data)
        return Response(data=data)

