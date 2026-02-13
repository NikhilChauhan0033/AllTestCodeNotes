from django.shortcuts import render
from django.contrib import messages
from .models import Calculation

# Create your views here.

def index(request):
    if request.method == "POST":
        try:
            name = None
            total = None

            name = request.POST.get('name')
            num1 = request.POST.get('num1')
            num2 = request.POST.get('num2')

            if not num1 and num2:
                messages.error(request,"Please enter number")
            else:
                total = int(num1) + int(num2)

                Calculation.objects.create(
                    name = name,
                    num1 = num1,
                    num2 = num2,
                    total = total
                )

                messages.success(request,"Calculation Saved Succesfully")

        except ValueError:
            messages.error(request,'Invalid number entered')

    calculations = Calculation.objects.all()

    return render(request,'index.html',{'calculations':calculations})

def delete_record(request,id):
    try:
        calculation = Calculation.objects.get(id=id)
        calculation.delete()
        messages.success(request,"Record Deleted Succesfully!!")
    except Exception as e:
        messages.error(request,f"Error deleting recortd : {str(e)}")


    calculations = Calculation.objects.all()
    return render(request,'index.html',{'calculations':calculations})

def edit_record(request,id):
    try:
        calculation = Calculation.objects.get(id=id)

        if request.method == "POST":
            name = request.POST.get('name')
            num1 = request.POST.get('num1')
            num2 = request.POST.get('num2')

            calculation.name = name
            calculation.num1 = num1
            calculation.num2 = num2
            calculation.total = int(num1) + int(num2)
            calculation.save()

            messages.success(request,"Record Updated Succesfullly!!")

            return render(request, 'index.html', {'calculations': Calculation.objects.all()})
        
        return render(request, 'edit.html', {'calculation': calculation})
    
    except Calculation.DoesNotExist:
        messages.error(request, "Record not found")
        return render(request, 'index.html', {'calculations': Calculation.objects.all()})
    except Exception as e:
        messages.error(request, f"Error editing record: {str(e)}")
        return render(request, 'index.html', {'calculations': Calculation.objects.all()})


