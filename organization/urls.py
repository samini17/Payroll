from django.urls import path

from .views import (EmployeeList, EmployeeDetailView,
                    SalaryPaymentView, DepartmentListView,
                    FurloughView, FurloughListView,
                    EmployerAccountView)

urlpatterns = [
    path('employers-list/', EmployeeList.as_view()),    # whole list of employers
    path('employers-list/<int:pk>/', EmployeeDetailView.as_view()),    # details of per employer
    path('salary/', SalaryPaymentView.as_view()),    # employer's salary
    path('departments/', DepartmentListView.as_view()),   # whole list of departments
    path('furlough/', FurloughView.as_view()),   # register furlough request
    path('furloughs-list/', FurloughListView.as_view()),   # whole of furloughs request
    path('register-employer/', EmployerAccountView.as_view())   # register employer
]
