from django.db import models
from django.utils.translation import ugettext_lazy as _
from utils.validators import validate_national_code, validate_phone_number


class Department(models.Model):
    name = models.CharField(_('name'), max_length=40)
    location = models.CharField(_('location'), max_length=40)
    address = models.TextField(_('address'), blank=True)
    established_date = models.DateField(_('established date'))
    avatar = models.ImageField(_('avatar'), blank=True, upload_to='department_avatars/')
    is_active = models.BooleanField(_('is_active'), default=True)

    class Meta:
        db_table = 'departments'
        verbose_name = _('Department')
        verbose_name_plural = _('Departments')

    def __str__(self):
        return self.name


class Employee(models.Model):
    SINGLE = 1
    MARRIED = 2
    DIVORCED = 3
    MARITAL_STATUS_CHOICES = (
        (SINGLE, _('single')),
        (MARRIED, _('married')),
        (DIVORCED, _('divorced'))
    )
    HELP_DESK = 4
    DEVELOPER = 5
    FINANCIAL = 6
    OPERATOR = 7
    JOB_TITLE_CHOICES = (
        (HELP_DESK, _('help desk')),
        (DEVELOPER, _('software developer')),
        (FINANCIAL, _('financial')),
        (OPERATOR, _('operator'))
    )

    first_name = models.CharField(_('first name'), max_length=40)
    last_name = models.CharField(_('last name'), max_length=40)
    national_code = models.CharField(_('national code'), validators=[validate_national_code],
                                     help_text=_('It must contain 10 digits...'), unique=True,
                                     max_length=10)
    phone_number = models.CharField(_('phone number'), validators=[validate_phone_number],
                                    help_text=_('It must be a VALID 12 digits like 98xxxxxxxxxx'), unique=True,
                                    max_length=12)
    age = models.PositiveSmallIntegerField(_('age'), default=18)
    job_title = models.PositiveSmallIntegerField(_('job title'), choices=JOB_TITLE_CHOICES, default=HELP_DESK)
    marital_status = models.PositiveSmallIntegerField(_('marital status'), choices=MARITAL_STATUS_CHOICES, default=SINGLE)
    date_joined = models.DateField(_('date joined'), auto_now_add=True)

    class Meta:
        db_table = 'employees'
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'

    def __str__(self):
        return f'{self.first_name} , {self.last_name}'


class Degree(models.Model):
    employee = models.ForeignKey(to=Employee, verbose_name=_('degree'), on_delete=models.SET_NULL, null=True)
    degree = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)
    avg = models.FloatField(default=0)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return '{} of- {}'.format(self.degree, self.branch)


class SalaryPayment(models.Model):
    employee = models.ForeignKey(to=Employee, verbose_name=_('employee'), on_delete=models.CASCADE)
    from_date = models.DateField(_('from date'))
    till_date = models.DateField(_('till date'))
    work_time = models.PositiveSmallIntegerField(_('work time'), default=0)
    wage = models.PositiveIntegerField(_('wage'), default=2000000)

    class Meta:
        db_table = 'payments'
        verbose_name = _('Payment')
        verbose_name_plural = _('Payments')


class Furlough(models.Model):
    employee = models.ForeignKey(to=Employee, verbose_name=_('employee'), on_delete=models.CASCADE)
    from_date = models.DateField(_('from date'))
    till_date = models.DateField(_('till date'))
    is_approved = models.BooleanField(default=False)

    class Meta:
        db_table = 'furloughs'
        verbose_name = _('Furlough')
        verbose_name_plural = _('Furloughs')



