from rest_framework import serializers
from website.models import Employee
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields = '__all__'