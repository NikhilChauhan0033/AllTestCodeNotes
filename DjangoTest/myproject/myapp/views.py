from django.shortcuts import render,redirect,get_object_or_404
from .models import ProductModel,StoreValue
from .serializers import ProductSerializers
from rest_framework import generics
from django.contrib import messages


# Create your views here.

class ProductView(generics.ListCreateAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializers

class ProductUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializers


def index(request):
    name = ''
    result = None
    if request.method == 'POST':
        name =  request.POST.get('name')
        num1 = int(request.POST.get('num1'))
        num2 = int(request.POST.get('num2'))

        result = num1+num2

        StoreValue.objects.create(name=name,num1=num1,num2=num2,result=result)

    all_values = StoreValue.objects.all()

    return render(request,'index.html',{'name':name,'result':result,'all_values':all_values})

def delete_view(request,id):
    value = get_object_or_404(StoreValue,id=id)

    if request.method == "POST":
        value.delete()
        messages.success(request,"Deleted Succesfully")

    return redirect('index')

def update_view(request,id):
    value = get_object_or_404(StoreValue,id=id)

    if request.method == 'POST':
        value.name = request.POST.get('name')
        value.num1 = int(request.POST.get('num1'))
        value.num2 = int(request.POST.get('num2'))
        value.result = value.num1 + value.num2
        value.save() #.save() updates instead of creating new row

        return redirect('index')
    
    messages.success(request,'Updated succesfully')
    
    return render(request,'update.html',{'value':value})