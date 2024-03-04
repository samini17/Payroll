from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Employee, Furlough, Department


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id', 'first_name', 'last_name', 'job_title')


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('id', 'name', 'location', 'established_date', 'is_active')


class FurloughSerializer(serializers.ModelSerializer):
    class Meta:
        model = Furlough
        fields = ('id', 'employee', 'from_date', 'till_date', 'is_approved')


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('first_name', 'last_name', 'national_code', 'phone_number')
        extra_kwargs = {
            'age': {'required': False},
            'job_title': {'required': False},
            'marital_status': {'required': False}
        }

    def create(self, validated_data):
        employer = Employee.objects.create(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            national_code=validated_data['national_code'],
            phone_number=validated_data['phone_number'],
            age=validated_data.get('age', 18),
            job_title=validated_data.get('job_title', 4),
            marital_status=validated_data.get('marital_status', 1)
        )
        return employer
