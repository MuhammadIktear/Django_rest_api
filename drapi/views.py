from django.shortcuts import render
from .models import Aiquest
from .serializers import AiquestsSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import io
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

# -------third approach-----

class AiquestCreate(APIView):
    def get(self,request,pk=None,format=None):
        id=pk
        #for models instance
        if id is not None:
            try:
                ai=Aiquest.objects.get(id=id) #colplex data
                serializer=AiquestsSerializer(ai)#python datatype/dict convert
                return Response(serializer.data)
            except Aiquest.DoesNotExist:
                return Response('No data found', status=status.HTTP_404_NOT_FOUND)
        #QuerySet(for all)
        ai=Aiquest.objects.all()#colplex data
        serializer=AiquestsSerializer(ai,many=True)#python datatype/dict convert
        return Response(serializer.data)
    
    def post(self,request,format=None):
        serializer=AiquestsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'Successfully saved data'}
            return Response(res)
        return Response(serializer.errors)
    
    def put(self,request,pk,format=None):
        id=pk
        ai=Aiquest.objects.get(pk=id)
        serializer=AiquestsSerializer(ai,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Full data updated'})
        return Response(serializer.errors)

    def patch(self,request,pk,format=None):
        id=pk
        ai=Aiquest.objects.get(pk=id)
        serializer=AiquestsSerializer(ai,data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial data updated'})
        return Response(serializer.errors)    
        
    def delete(self,request,pk,format=None):
        id=pk
        ai=Aiquest.objects.get(pk=id)
        ai.delete()    
        return Response({'msg':'Successfully deleted'})



# -------Second approach-----
# @api_view(['GET','POST','PUT','PATCH','DELETE'])
# def aiquest_create(request,pk=None):
#     if request.method=='GET':
#         id=pk
#         #for models instance
#         if id is not None:
#             try:
#                 ai=Aiquest.objects.get(id=id) #colplex data
#                 serializer=AiquestsSerializer(ai)#python datatype/dict convert
#                 return Response(serializer.data)
#             except Aiquest.DoesNotExist:
#                 return Response('No data found', status=status.HTTP_404_NOT_FOUND)
#         #QuerySet(for all)
#         ai=Aiquest.objects.all()#colplex data
#         serializer=AiquestsSerializer(ai,many=True)#python datatype/dict convert
#         return Response(serializer.data)
    
#     if request.method=='POST':
#         serializer=AiquestsSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             res={'msg':'Successfully saved data'}
#             return Response(res)
#         return Response(serializer.errors)
    
#     if request.method=='PUT':
#         id=pk
#         ai=Aiquest.objects.get(pk=id)
#         serializer=AiquestsSerializer(ai,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Full data updated'})
#         return Response(serializer.errors)

#     if request.method=='PATCH':
#         id=pk
#         ai=Aiquest.objects.get(pk=id)
#         serializer=AiquestsSerializer(ai,data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Partial data updated'})
#         return Response(serializer.errors)    
        
#     if request.method=='DELETE':
#         id=pk
#         ai=Aiquest.objects.get(pk=id)
#         ai.delete()    
#         return Response({'msg':'Successfully deleted'})





# -------first approach-----
# # Create your views here.
# #QuerySet
# #for serilizarion(get all info)
# def aiquest_info(request):
#     #complex_data
#     ai=Aiquest.objects.all()
#     #python dict
#     serializer=AiquestsSerializer(ai,many=True)
#     #Json render
#     json_data=JSONRenderer().render(serializer.data)
#     #json sent to user
#     return HttpResponse(json_data,content_type='application/json')

# #model instance 
# #for serilizarion(get perticular info using pk)
# def aiquest_inst(request,pk):
#     #complex_data
#     ai=Aiquest.objects.get(id=pk)
#     #python dict
#     serializer=AiquestsSerializer(ai)
#     #Json render
#     json_data=JSONRenderer().render(serializer.data)
#     #json sent to user
#     return HttpResponse(json_data,content_type='application/json')

# #for Deserilizarion(create)
# @csrf_exempt
# def aiquest_create(request):
#     if request.method=='POST':
#         json_data=request.body #user er deya json data gulo json_data ei save hobe       
#         stream=io.BytesIO(json_data)#json to stream convert
#         pythondata=JSONParser().parse(stream)#stream to python data
#         serializer=AiquestsSerializer(data=pythondata)
#         if serializer.is_valid():
#             serializer.save()
#             res={'msg':'Successfully insert data'}
#             json_data=JSONRenderer().render(res)
#             return HttpResponse(json_data,content_type='application/json')
#         json_data=JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data,content_type='application/json') 
    
# #for Deserilizarion(update)            
#     if request.method=='PUT':
#         json_data=request.body
#         stream=io.BytesIO(json_data)
#         pythondata=JSONParser().parse(stream)
#         id=pythondata.get('id')
#         aiq=Aiquest.objects.get(id=id)
#         serializer=AiquestsSerializer(aiq,data=pythondata,partial=True)
#         #pertial data True mane sudu je data gula ami update korte chacchi segula ami korte parbo jodi partial na ditam thaole amarder pura model instance update korte hoto
#         if serializer.is_valid():
#             serializer.save()
#             res={'msg':'Successfully update data'}
#             json_data=JSONRenderer().render(res)
#             return HttpResponse(json_data,content_type='application/json')  
#         json_data=JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data,content_type='application/json')  
    
# #delete models instance/object    
#     if request.method == 'DELETE':
#         json_data=request.body
#         stream=io.BytesIO(json_data)
#         pythondata=JSONParser().parse(stream)
#         id=pythondata.get('id')
#         aiq=Aiquest.objects.get(id=id)
#         aiq.delete()
#         res={'msg':'Successfully deleted data'}
#         json_data=JSONRenderer().render(res)
#         return HttpResponse(json_data,content_type='application/json')          
                
        
        
        
    