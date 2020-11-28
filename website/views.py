from django.shortcuts import render

# Create your views here.
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from website.models import Employee
from website.serialaizer import EmployeeSerializer
def index(request):
    return render(request,'index.html')
class employeelist(APIView):
 def get(self,request):
    emp=Employee.objects.all()
    serialiser=EmployeeSerializer(emp,many=True)
    x=serialiser.data
    print(emp)
    args={'emp':emp}
    #print(pd.DataFrame(val1, columns=["time", "temperature", "quality"]))
    #return render(request,'muni.html',args)
    return Response(x)
 def put(self):
    return None