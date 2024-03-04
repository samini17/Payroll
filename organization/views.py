from rest_framework.views import APIView
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.db.models import Sum

from .models import Employee, SalaryPayment, Department, Furlough
from .serializers import EmployeeSerializer, DepartmentSerializer, FurloughSerializer, RegisterSerializer


class EmployeeList(APIView):
    """
    :return the whole of employers list
    """

    def get(self, request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)


class EmployeeDetailView(APIView):
    permission_classes = [IsAuthenticated]
    """
    :return return detail of each employer
    """

    def get(self, request, pk):
        try:
            employee = Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = EmployeeSerializer(employee, context={'request': request})
        return Response(serializer.data)


class SalaryPaymentView(APIView):
    permission_classes = [IsAuthenticated]
    """
    Calculate the salary of each employer and return it
    """
    def post(self, request):

        try:
            national_code = request.data.get('national_code')
            employee = Employee.objects.get(national_code=national_code)
        except Employee.DoesNotExist:
            return Response({"detail': 'Employer doesn't exist"},
                            status=status.HTTP_404_NOT_FOUND)
        try:
            s = SalaryPayment.objects.annotate(salary=Sum('work_time') * Sum('wage'))
            pk = employee.pk
            return Response({'salary': s[pk - 1].salary, 'name': employee.first_name, 'family': employee.last_name})
        except Exception:
            return Response({'detail': 'Salary has not determined yet!'},
                            status=status.HTTP_404_NOT_FOUND)


class DepartmentListView(APIView):
    """
    :return whole list of departments
    """
    def get(self, request):
        departments = Department.objects.all()
        serializer = DepartmentSerializer(departments, many=True)
        return Response(serializer.data)


class FurloughView(APIView):
    permission_classes = [IsAuthenticated]
    """
    It takes 3 arguments(national code, start date, end date) from import and registers a furlough request.
    """
    def post(self, request):
        try:
            national_code = request.data.get('national_code')
            employee = Employee.objects.get(national_code=national_code)
        except Employee.DoesNotExist:
            return Response({"detail': 'Employer doesn't exist"},
                            status=status.HTTP_404_NOT_FOUND)

        from_date = request.data.get('from_date')
        till_date = request.data.get('till_date')
        f = Furlough.objects.create(employee=employee, from_date=from_date, till_date=till_date, is_approved=False)

        f.save()
        return Response(status=status.HTTP_200_OK)


class FurloughListView(APIView):
    permission_classes = [IsAuthenticated]
    """
    :return all of employer's request's furloughs
    """
    def get(self, request):
        furloughs = Furlough.objects.all()
        serializer = FurloughSerializer(furloughs, many=True)
        return Response(serializer.data)


class EmployerAccountView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    """
    It's for registering employers,you should import[first_name, last_name, national_code, phone_number]
    """
    queryset = Employee.objects.all()
    serializer_class = RegisterSerializer


