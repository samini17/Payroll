from django import template

from organization.models import SalaryPayment, Employee

register = template.Library()


@register.simple_tag
def times(self):
    work_time = SalaryPayment.objects.get('work_time')
    hourly_wage_base = SalaryPayment.objects.get('hourly_wage_base')
    return hourly_wage_base * work_time
