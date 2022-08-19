from functools import partial
from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .models import Students
from .serializers import StudentSerializers
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def Students_api(request):
    print("--------",request)
    print("========",request.body)
    if request.method == 'GET':

        json_data = request.body
        # print(request.body)  
        # json_data ={'name':'wajahat'}
        stream = io.BytesIO(json_data)
        print(stream)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id', None)
        if id is not None:
            stu = Students.objects.get(id= id)
            serializer = StudentSerializers(stu)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')
        else:
            stu = Students.objects.all()
            serializer = StudentSerializers(stu, many=True)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')



            
    if request.method == 'POST':
            json_data = request.body
            stream = io.BytesIO(json_data)
            pythondata = JSONParser().parse(stream)
            serializer = StudentSerializers(data = pythondata)
            if serializer.is_valid():
                serializer.save()
                res = {'msg': 'Data created'}
                json_data = JSONRenderer().render(res)
                return HttpResponse(json_data, content_type='application/json')
            json_data = JSONRenderer().render(serializer.errors)
            return HttpResponse(json_data, content_type='application/json')



    if request.method == 'PUT':
        print("helllllllllllllllllll")
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = Students.objects.get(id=id)
        serializer = StudentSerializers(stu, data=pythondata)
        # print(""serializer)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data Updated !!'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        else:
            json_data = JSONRenderer().render(serializer.errors)
            return HttpResponse(json_data, content_type='application/json')


                
    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = Students.objects.get(id = id)
        stu.delete()
        res = {'msg': 'Data Deleted!!'}
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data, content_type='application/json')

